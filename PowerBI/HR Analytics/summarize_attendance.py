"""Convert the April–June 2022 attendance workbook into month/weekday totals."""
import argparse
import csv
from collections import defaultdict
from datetime import date
from pathlib import Path

from openpyxl import load_workbook


FIELDS = ("month", "weekday_number", "weekday", "recorded_workdays", "present_days",
          "remote_days", "sick_days")
WEEKDAYS = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")
FULL_LEAVE = {"PL", "SL", "FFL", "BL", "LWP", "BRL", "ML"}
HALF_LEAVE = {"H" + code for code in FULL_LEAVE}


def summarize(source):
    workbook = load_workbook(source, read_only=True, data_only=True)
    totals = defaultdict(lambda: [0, 0.0, 0.0, 0.0])
    seen = set()
    try:
        for sheet in workbook:
            rows = iter(sheet.values)
            date_row = next(rows, ())
            dates = {i: value.date() if hasattr(value, "date") else value
                     for i, value in enumerate(date_row) if isinstance(value, date)}
            if not dates:
                continue
            headers = next(rows, ())
            if tuple(str(cell).strip() for cell in headers[:2]) != ("Employee Code", "Name"):
                raise ValueError("Unexpected monthly sheet layout")
            for row in rows:
                if not any(row[i] for i in dates):
                    continue
                if not row[0] or not row[1]:
                    raise ValueError("A dated entry is missing a worker identifier")
                for i, day in dates.items():
                    code = str(row[i] or "").strip()
                    if not code:
                        continue
                    # Some worker codes recur with different names in the workbook.
                    key = (str(row[0]).strip(), str(row[1]).strip().casefold(), day)
                    if key in seen:
                        raise ValueError("Two populated entries for the same worker and date")
                    seen.add(key)
                    if code in {"WO", "HO"}:
                        continue
                    if code not in FULL_LEAVE | HALF_LEAVE | {"P", "WFH", "HWFH"}:
                        raise ValueError("Unknown attendance status code")
                    bucket = totals[day.strftime("%Y-%m"), day.weekday()]
                    bucket[0] += 1
                    if code in {"P", "WFH", "HWFH"}:
                        bucket[1] += 1
                    elif code in HALF_LEAVE:
                        bucket[1] += 0.5
                    if code in {"WFH", "HWFH"}:
                        bucket[2] += 1 if code == "WFH" else 0.5
                    if code in {"SL", "HSL"}:
                        bucket[3] += 1 if code == "SL" else 0.5
    finally:
        workbook.close()
    if not totals:
        raise ValueError("No recorded workdays in the workbook")
    for (month, weekday), values in sorted(totals.items()):
        yield (month, weekday + 1, WEEKDAYS[weekday], *values)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("workbook", type=Path)
    parser.add_argument("output", type=Path)
    args = parser.parse_args()
    if args.workbook.resolve() == args.output.resolve():
        parser.error("Select separate input and output files")
    results = list(summarize(args.workbook))
    with args.output.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.writer(handle, lineterminator="\n")
        writer.writerow(FIELDS)
        writer.writerows(results)
