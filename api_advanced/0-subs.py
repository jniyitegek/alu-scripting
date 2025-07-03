#!/usr/bin/python3
"""
This module provides a function to retrieve the number of subscribers
for a given subreddit using Reddit's public API.

Functions:
    the number of subscribers for a subreddit.
"""
import requests


def number_of_subscribers(subreddit):
    """Returns the number of subscribers for a given subreddit."""
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {'User-Agent': 'Python:subscribers:v1.0 (by /u/yourusername)'}
    try:
        response = requests.get(url, headers=headers,
                                allow_redirects=False, timeout=10)
        if response.status_code == 200:
            data = response.json()
            return data.get('data', {}).get('subscribers', 0)
        else:
            return 0
    except Exception:
        return 0
