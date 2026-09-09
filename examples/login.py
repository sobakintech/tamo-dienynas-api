"""Log in and inspect the number of account roles without printing credentials."""

import argparse

from _client import print_content, run_authenticated


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--show-role-labels", action="store_true", help="Print role labels, which can contain names and school information")
    args = parser.parse_args()

    def show_roles(client):
        roles = client.roles()
        print(f"Login accepted. Roles returned: {len(roles)}")
        print("The token is held in memory and is not printed or saved.")
        if args.show_role_labels:
            print_content([
                {"index": index, "title": role.get("title"), "subtitle": role.get("subtitle")}
                for index, role in enumerate(roles)
            ])

    return run_authenticated(show_roles)


if __name__ == "__main__":
    raise SystemExit(main())
