#!/usr/bin/python3
"""This  retrieve posts from a given subreddit using Reddit's public API.

Modules:
    requests: Allows sending HTTP requests to interact with the Reddit API.
"""
import requests

"""This  function retrieve data from api"""
def recurse(subreddit, hot_list=None, after=None):
    """Get data from api."""
    if hot_list is None:
        hot_list = []
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {'User-Agent': 'python:recurse:v1.0 (by /u/yourusername)'}
    params = {'limit': 100}
    if after:
        params['after'] = after

    try:
        response = requests.get(url, headers=headers,
                                params=params, allow_redirects=False)
        if response.status_code != 200:
            return None
        data = response.json().get('data', {})
        posts = data.get('children', [])
        for post in posts:
            hot_list.append(post['data'].get('title'))
        after = data.get('after')
        if after:
            return recurse(subreddit, hot_list, after)
        return hot_list
    except Exception:
        return None
