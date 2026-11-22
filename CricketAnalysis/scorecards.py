"""Rebuild the men's 2022 T20 World Cup model and rank players from archived scorecards."""
import argparse
import json
import re
from pathlib import Path

import pandas as pd


DATA = Path(__file__).resolve().parent / 'data'


def player_name(value):
    # Captain and wicketkeeper marks belong to the appearance, not the player's name.
    return re.sub(r'\s*\(c\)', '', value.replace('†', '').replace('\xa0', ' ')).strip()


def legal_balls(overs):
    match = re.fullmatch(r'(\d+)(?:\.([0-5]))?', str(overs))
    if not match:
        raise ValueError(f'Invalid cricket overs notation: {overs!r}')
    return 6 * int(match.group(1)) + int(match.group(2) or 0)


def read_json(raw, name):
    return json.loads((raw / f't20_wc_{name}.json').read_text(encoding='utf-8'))


def build_tables(raw=DATA / 'raw'):
    matches = pd.DataFrame(read_json(raw, 'match_results')[0]['matchSummary'])
    matches = matches.rename(columns={'scorecard': 'match_id'})
    if not matches['match_id'].is_unique:
        raise ValueError('Match IDs must be unique')
    match_keys = {}
    for row in matches.itertuples(index=False):
        for pair in [(row.team1, row.team2), (row.team2, row.team1)]:
            label = ' Vs '.join(pair)
            if label in match_keys:
                raise ValueError(f'Ambiguous fixture {label}; use a scorecard ID to join')
            match_keys[label] = row.match_id

    def innings(kind, player_field):
        rows = [row for group in read_json(raw, kind + '_summary')
                for row in group[kind + 'Summary']]
        frame = pd.DataFrame(rows)
        frame[player_field] = frame[player_field].map(player_name)
        frame['match_id'] = frame['match'].map(match_keys)
        if frame['match_id'].isna().any():
            raise ValueError(f'Unknown fixture in {kind} records')
        return frame

    batting = innings('batting', 'batsmanName')
    dismissed = batting.pop('dismissal').str.strip().ne('')
    batting['out/not_out'] = dismissed.map({True: 'out', False: 'not_out'})
    bowling = innings('bowling', 'bowlerName')
    bowling['legal_balls'] = bowling['overs'].map(legal_balls)

    players = pd.DataFrame(read_json(raw, 'player_info'))
    players['name'] = players['name'].map(player_name)
    players = players.drop_duplicates()
    media = pd.read_csv(raw / 'player_enrichment.csv', keep_default_na=False)
    players = players.merge(media, on=['team', 'name'], how='left', validate='one_to_one')
    known_players = set(zip(players['team'], players['name']))
    for frame, team, name in [(batting, 'teamInnings', 'batsmanName'),
                              (bowling, 'bowlingTeam', 'bowlerName')]:
        if not set(zip(frame[team], frame[name])).issubset(known_players):
            raise ValueError('Unmatched scorecard player')
        if frame.duplicated(['match_id', team, name]).any():
            raise ValueError('Repeated player appearance in the same innings')
    return {'dim_match_summary': matches, 'dim_players': players,
            'fact_batting_summary': batting, 'fact_bowling_summary': bowling}


def rankings(tables):
    batting = tables['fact_batting_summary'].copy()
    bowling = tables['fact_bowling_summary'].copy()
    batting[['runs', 'balls']] = batting[['runs', 'balls']].apply(pd.to_numeric)
    bowling[['runs', 'wickets']] = bowling[['runs', 'wickets']].apply(pd.to_numeric)
    bat = batting.groupby(['teamInnings', 'batsmanName'], as_index=False).agg(
        innings=('match_id', 'size'), runs=('runs', 'sum'), balls=('balls', 'sum'))
    bat['strike_rate'] = (100 * bat['runs'] / bat['balls'].where(bat['balls'] > 0)).round(2)
    bowl = bowling.groupby(['bowlingTeam', 'bowlerName'], as_index=False).agg(
        wickets=('wickets', 'sum'), runs=('runs', 'sum'), legal_balls=('legal_balls', 'sum'))
    bowl['economy'] = (6 * bowl['runs'] / bowl['legal_balls'].where(bowl['legal_balls'] > 0)).round(2)
    return (bat.sort_values(['runs', 'batsmanName'], ascending=[False, True]),
            bowl.sort_values(['wickets', 'bowlerName'], ascending=[False, True]))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, help='also write the four model CSVs into this directory')
    args = parser.parse_args()
    tables = build_tables()
    if args.output:
        args.output.mkdir(exist_ok=True, parents=True)
        for name, table in tables.items():
            table.to_csv(args.output / f'{name}.csv', index=False, lineterminator='\n')
    for ranked in rankings(tables):
        print(ranked.head(5).to_string(index=False), end='\n\n')


if __name__ == '__main__':
    main()
