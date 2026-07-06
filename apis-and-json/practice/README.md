# Practice: Fetch a GitHub user

## Your task

Complete `practice/github_user.py` so that it:

1. Asks for a GitHub username (or hardcode one to start).
2. Calls the GitHub API: `https://api.github.com/users/<username>`.
3. Parses the JSON and prints: `name`, `public_repos`, `followers`, `location`.
4. Saves the full response to `github_user.json` using `json.dump(..., indent=2)`.
5. Bonus: handle a non-existent user gracefully (GitHub returns 404) using
   `response.raise_for_status()` inside a `try / except`.

## Run it

```bash
python practice/github_user.py
```

## Done?

Compare with [`../solution/github_user.py`](../solution/github_user.py).
