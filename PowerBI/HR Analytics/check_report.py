"""Check that the published, aggregate-only CSV matches the offline Power BI source."""
import csv
import json
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parent

def verify():
    project = json.loads((ROOT / 'Presence Insights.pbip').read_text(encoding='utf-8'))
    report = ROOT / project['artifacts'][0]['report']['path']
    definition = json.loads((report / 'definition.pbir').read_text(encoding='utf-8'))
    model = report / definition['datasetReference']['byPath']['path']
    table = (model / 'definition/tables/Attendance.tmdl').read_text(encoding='utf-8')
    header_line = next(line for line in table.splitlines() if line.strip().startswith('headers = {'))
    expected_header = re.findall(r'"([^"]+)"', header_line)
    rows = [re.findall(r'"([^"]*)"', line) for line in table.splitlines()
            if line.lstrip().startswith('{"20')]
    with (ROOT / 'attendance_summary.csv').open(encoding='utf-8', newline='') as stream:
        actual = list(csv.reader(stream))
    if [expected_header, *rows] != actual:
        raise ValueError('The Power BI offline source and attendance_summary.csv differ')
    if expected_header != ['month', 'weekday_number', 'weekday', 'recorded_workdays',
                           'present_days', 'remote_days', 'sick_days']:
        raise ValueError('Unexpected aggregate dataset columns')
    if not rows or len({(r[0], r[1]) for r in rows}) != len(rows):
        raise ValueError('Expected one row per month and weekday')
    for file in (report / 'definition').rglob('*.json'):
        json.loads(file.read_text(encoding='utf-8'))
    print(f'Verified {len(rows)} month/weekday aggregates in the Power BI source.')

if __name__ == '__main__':
    verify()
