"""Read a calendar week using the Monday-aligned modern API request."""

import argparse
from datetime import timedelta

from _client import ApiError, choose_role, current_monday, iso_date, print_content, require_list, run_authenticated


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--date", type=iso_date, default=current_monday(), help="Any date in the desired week, YYYY-MM-DD")
    parser.add_argument("--role-index", type=int, help="Zero-based index in the roles returned by this login")
    parser.add_argument("--show-content", action="store_true", help="Print selected calendar fields, including private school content")
    args = parser.parse_args()
    if args.role_index is not None and args.role_index < 0:
        parser.error("--role-index must be zero or greater.")
    monday = args.date - timedelta(days=args.date.weekday())

    def show_calendar(client):
        role = choose_role(client.roles(), args.role_index)
        payload = client.calendar(role, monday)
        days = require_list(payload, "days")
        count = 0
        selected_days = []
        fields = ("timeFromUtc", "timeToUtc", "eventTitle", "eventSubtitle", "eventDescription")
        for day in days:
            if not isinstance(day, dict):
                raise ApiError("Unexpected calendar day shape.")
            events = require_list(day, "events")
            if any(not isinstance(event, dict) for event in events):
                raise ApiError("Unexpected calendar event shape.")
            count += len(events)
            if args.show_content:
                selected_days.append({
                    "date": day.get("date"),
                    "events": [{key: event.get(key) for key in fields} for event in events],
                })
        print(f"Week starting {monday}: {len(days)} days, {count} events")
        if args.show_content:
            print_content(selected_days)

    return run_authenticated(show_calendar)


if __name__ == "__main__":
    raise SystemExit(main())
