import os
import unittest
from unittest.mock import patch

import requests

from main import app, recommendations


class MovieAppTests(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()
        self.offline = patch.dict(os.environ, {"TMDB_KEY": ""})
        self.offline.start()
        self.addCleanup(self.offline.stop)

    def test_search_form_and_unknown_title(self):
        self.assertIn(b'Find films similar to', self.client.get('/').data)
        response = self.client.get('/recommend', query_string={'title': 'not a real title 97821'})
        self.assertEqual(response.status_code, 404)
        self.assertIn(b'Choose a title', response.data)

    def test_recommendations_are_distinct_and_case_insensitive(self):
        with patch('main.requests.get', side_effect=AssertionError('Unexpected network access')):
            response = self.client.get('/recommend', query_string={'title': '  THE   matrix  '})
            self.assertEqual(response.status_code, 200)
            self.assertIn(b'The Matrix Reloaded', response.data)
            related = recommendations('The Matrix', 5)
            self.assertEqual(related, recommendations('the matrix', 5))
            self.assertEqual(len(set(related)), 5)
            self.assertNotIn('the matrix', related)
            reply = self.client.post('/similarity', data={'name': 'The Matrix'})
            self.assertEqual(reply.get_data(as_text=True).split('---')[:5], related)

    def test_local_review_is_classified(self):
        response = self.client.post('/recommend', data={
            'title': 'Avatar', 'review': 'An excellent and enjoyable film.',
        })
        self.assertEqual(response.status_code, 200)
        self.assertRegex(response.data, rb'<strong>(Positive|Negative)</strong>')
        self.assertIn(b'An excellent and enjoyable film.', response.data)

    def test_optional_service_failure_falls_back_to_local_data(self):
        with patch.dict(os.environ, {'TMDB_KEY': 'dummy'}), \
             patch('main.requests.get', side_effect=requests.Timeout):
            page = self.client.get('/recommend', query_string={'title': 'Avatar'})
            self.assertEqual(page.status_code, 200)
            self.assertIn(b'Live movie details are unavailable', page.data)
            self.assertIn(b'Similar films', page.data)

    def test_enriched_movie_and_cast_serialization(self):
        def stub(endpoint, **params):
            return {
                'search/movie': {'results': [{'id': 1, 'title': 'Avatar'}]},
                'movie/1': {'credits': {'cast': [{'id': 2, 'name': 'Example Actor', 'character': 'Pilot'}]},
                            'reviews': {'results': [{'content': 'I enjoyed this movie.'}]}},
                'person/2': {'name': 'Example Actor', 'biography': 'Example biography.'},
            }.get(endpoint, {})
        with patch('main.tmdb_get', side_effect=stub):
            page = self.client.get('/recommend?title=Avatar')
            self.assertEqual(page.status_code, 200)
            self.assertIn(b'/cast/2', page.data)
            self.assertIn(b'I enjoyed this movie.', page.data)
            self.assertIn(b'Example biography.', self.client.get('/cast/2').data)
            self.assertEqual(self.client.get('/cast/3').status_code, 404)


if __name__ == '__main__':
    unittest.main()
