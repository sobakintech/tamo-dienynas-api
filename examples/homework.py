"""Read homework or classwork for a bounded date range. Does not mark completion."""

import argparse
from datetime import timedelta

from _client import choose_role, current_monday, iso_date, print_content, require_list, run_authenticated


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--from", dest="start", type=iso_date, help="First date, YYYY-MM-DD; defaults to this Monday")
    parser.add_argument("--to", dest="end", type=iso_date, help="Last date, YYYY-MM-DD; defaults to six days after --from")
    parser.add_argument("--work-type", choices=("home", "class"), default="home")
    parser.add_argument("--role-index", type=int, help="Zero-based index in the roles returned by this login")
    parser.add_argument("--show-content", action="store_true", help="Print selected homework fields, including private school content")
    args = parser.parse_args()
    start = args.start or current_monday()
    try:
        end = args.end or start + timedelta(days=6)
    except OverflowError:
        parser.error("The date range exceeds supported calendar dates.")
    if not 0 <= (end - start).days <= 30:
        parser.error("Choose an ordered date range of at most 31 calendar days.")
    if args.role_index is not None and args.role_index < 0:
        parser.error("--role-index must be zero or greater.")

    def show_homework(client):
        role = choose_role(client.roles(), args.role_index)
        payload = client.homework(role, start, end, args.work_type)
        items = require_list(payload, "items")
        if any(not isinstance(item, dict) for item in items):
            parser.exit(1, "Error: unexpected work item shape.\n")
        print(f"{args.work_type}: {len(items)} items for {start} through {end}")
        if args.show_content:
            fields = ("thingName", "date", "deadline", "homeWork", "completionDate")
            print_content([{key: item.get(key) for key in fields} for item in items])

    return run_authenticated(show_homework)


if __name__ == "__main__":
    raise SystemExit(main())
