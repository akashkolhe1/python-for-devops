# Working with APIs & JSON

Clouds, Kubernetes, monitoring and CI/CD all speak HTTP and JSON, so calling
APIs is a big part of DevOps automation. This module covers how to call them and
handle their data in Python.

You'll use the [`requests`](https://docs.python-requests.org/) library to call
public APIs, parse the JSON responses, extract what you need with dictionaries
and lists, and save results to a JSON file.

---

## Learning objectives

- Call a public API with `requests.get()`
- Parse a JSON response with `.json()`
- Work with Python collections: `list`, `dict`, `set`
- Read from and write to files (including `json.dump` / `json.load`)
- Keep secrets (API keys) out of source code using environment variables

---

## Setup

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## What's inside

```
apis-and-json/
├── examples/
│   ├── collections_demo.py     # list / dict / set essentials
│   ├── call_api.py             # JSONPlaceholder: fetch + filter todos
│   ├── jokes_api.py            # switching between multiple endpoints + headers
│   ├── file_io.py              # read + write text and JSON files
│   └── stock_market_api.py     # real API using an env-var API key (no secrets!)
├── practice/
│   ├── github_user.py          # fetch a GitHub user and save to JSON
│   └── README.md
└── solution/
    └── github_user.py
```

## How to run

```bash
python examples/collections_demo.py
python examples/call_api.py
python examples/jokes_api.py
python examples/file_io.py

# stock_market_api needs a free Alpha Vantage key (see below)
export ALPHAVANTAGE_API_KEY="your_key_here"
python examples/stock_market_api.py
```

Never hardcode API keys in source. `stock_market_api.py` reads the key from the
`ALPHAVANTAGE_API_KEY` environment variable. Get a free key at
https://www.alphavantage.co/support/#api-key

## Practice

Complete `practice/github_user.py` — see [`practice/README.md`](practice/README.md).
