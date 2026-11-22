"""Regression checks for overs and player identity across exported scorecards."""
import unittest
from scorecards import build_tables, legal_balls, player_name, rankings


class ScorecardsTest(unittest.TestCase):
    def test_partial_over(self):
        self.assertEqual(legal_balls('3.2'), 20)
        with self.assertRaises(ValueError):
            legal_balls('3.6')

    def test_scorecard_marks(self):
        self.assertEqual(player_name('Matthew Wade(c)†'), player_name('Matthew Wade†'))

    def test_published_tournament(self):
        tables = build_tables()
        self.assertEqual(len(tables['dim_match_summary']), 45)
        self.assertEqual(len(tables['dim_players']), 213)
        self.assertEqual(tables['fact_batting_summary']['match_id'].nunique(), 42)
        bat, bowl = rankings(tables)
        self.assertEqual(tuple(bat.iloc[0][['batsmanName', 'runs', 'balls']]),
                         ('Virat Kohli', 296, 217))
        self.assertEqual(tuple(bowl.iloc[0][['bowlerName', 'wickets', 'legal_balls']]),
                         ('Wanindu Hasaranga de Silva', 15, 186))
