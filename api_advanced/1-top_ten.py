#!/usr/bin/python3
"""Script that fetch 10 hot post for a given subreddit."""


import requests


def top_ten(subreddit):
    """Return number of subscribers if @subreddit is valid subreddit.
    if not return 0."""

    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {
        "User-Agent": "MyRedditApp/1.0"
    }
    params = {"limit": 10}

    response = requests.get(url, headers=headers,
                            params=params, allow_redirects=False)

    if response.status_code != 200:
        print(None)
        return

    data = response.json()
    posts = data.get("data", {}).get("children", [])
    if not posts:
        print(None)
        return

    for post in posts:
        print(post["data"]["title"])
