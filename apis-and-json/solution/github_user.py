# Fetch a GitHub user and save the response to JSON.

import json
from pathlib import Path

import requests

OUTPUT_FILE = Path(__file__).parent / "github_user.json"


def fetch_github_user(username):
    url = f"https://api.github.com/users/{username}"
    response = requests.get(url, timeout=10)
    response.raise_for_status()
    return response.json()


def main():
    username = input("GitHub username: ").strip() or "LondheShubham153"

    try:
        user = fetch_github_user(username)
    except requests.HTTPError as exc:
        print(f"Could not fetch '{username}': {exc}")
        return

    for field in ("name", "public_repos", "followers", "location"):
        print(f"{field:13}: {user.get(field)}")

    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        json.dump(user, f, indent=2)
    print(f"\nSaved full response to {OUTPUT_FILE.name}")


if __name__ == "__main__":
    main()
