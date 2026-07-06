# Practice: fetch a GitHub user and save the response to JSON.

import requests  # noqa: F401  (you'll use this)


def fetch_github_user(username):
    # TODO 1: build the URL https://api.github.com/users/<username>
    # TODO 2: GET it with timeout=10, then .json()
    # TODO 3: return the dict
    raise NotImplementedError("Implement fetch_github_user")


def main():
    username = input("GitHub username: ").strip() or "LondheShubham153"
    user = fetch_github_user(username)

    # TODO 4: print name, public_repos, followers, location
    # TODO 5: save `user` to github_user.json with json.dump(..., indent=2)
    print(user)


if __name__ == "__main__":
    main()
