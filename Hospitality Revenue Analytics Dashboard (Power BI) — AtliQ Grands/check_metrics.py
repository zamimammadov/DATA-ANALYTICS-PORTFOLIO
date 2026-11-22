"""Reconcile the two booking facts and reproduce the report's unfiltered KPIs."""

import csv
from collections import Counter, defaultdict
from datetime import date
from pathlib import Path

DATA = Path(__file__).resolve().parent / "ExcelDatas"
MONTHS = "Jan Feb Mar Apr May Jun Jul Aug Sep Oct Nov Dec".split()


def rows(filename):
    with (DATA / filename).open(encoding="utf-8-sig", newline="") as stream:
        yield from csv.DictReader(stream)


def inventory_date(value):
    day, month, year = value.split("-")
    return date(2000 + int(year), MONTHS.index(month) + 1, int(day))


def day_group(check_in):
    # The DAX calculated column in metrics-list.xlsx uses Friday and Saturday.
    return "Weekend (Fri/Sat)" if check_in.weekday() in (4, 5) else "Weekday (Sun–Thu)"


def main():
    categories = {row["property_id"]: row["category"] for row in rows("dim_hotels.csv")}
    revenue_by_category = Counter()
    days = defaultdict(Counter)
    reservations = Counter()
    booking_ids = set()
    for row in rows("fact_bookings.csv"):
        booking = row["booking_id"]
        if booking in booking_ids:
            raise ValueError(f"Duplicate booking ID: {booking}")
        booking_ids.add(booking)
        check_in = date.fromisoformat(row["check_in_date"])
        cell = (row["property_id"], check_in, row["room_category"])
        reservations[cell] += 1
        realised = int(row["revenue_realized"])
        revenue_by_category[categories[row["property_id"]]] += realised
        totals = days[day_group(check_in)]
        totals["revenue"] += realised
        totals["bookings"] += 1
        totals[row["booking_status"]] += 1

    inventory_keys = set()
    for row in rows("fact_aggregated_bookings.csv"):
        check_in = inventory_date(row["check_in_date"])
        cell = (row["property_id"], check_in, row["room_category"])
        if cell in inventory_keys:
            raise ValueError(f"Duplicate inventory key: {cell}")
        inventory_keys.add(cell)
        if reservations[cell] != int(row["successful_bookings"]):
            raise ValueError(f"Booking count differs between facts: {cell}")
        days[day_group(check_in)]["capacity"] += int(row["capacity"])
    if reservations.keys() - inventory_keys:
        raise ValueError("Bookings have no corresponding inventory rows")

    overall = sum(days.values(), Counter())
    print(f"Source: {overall['bookings']:,} bookings, {len(inventory_keys):,} inventory rows, "
          f"{overall['capacity']:,} available slots.")
    print(f"{'Check-in group':<20} {'Revenue (INR)':>16} {'Occupancy':>12} "
          f"{'ADR (INR)':>12} {'RevPAR (INR)':>14} {'Realisation':>12}")
    for label, values in [("All", overall), *sorted(days.items())]:
        bookings, capacity, revenue = values["bookings"], values["capacity"], values["revenue"]
        print(f"{label:<20} {revenue:>16,} {bookings / capacity:>12.2%} "
              f"{revenue / bookings:>12,.2f} {revenue / capacity:>14,.2f} "
              f"{values['Checked Out'] / bookings:>12.2%}")
    print(f"Cancelled: {overall['Cancelled']:,} ({overall['Cancelled'] / overall['bookings']:.2%})")
    for category, revenue in sorted(revenue_by_category.items()):
        print(f"{category}: INR {revenue:,} ({revenue / overall['revenue']:.2%} of revenue)")


if __name__ == "__main__":
    main()
