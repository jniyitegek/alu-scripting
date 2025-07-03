#!/usr/bin/python3
"""
This module provides of hot posts from a given subreddit using the Reddit API.

Modules:
    requests: For making HTTP requests to the Reddit API.
    re: For regular expression operations to extract words from post titles.
"""

import requests
import re


def count_words(subreddit, word_list, after=None, counts=None):
    """Count words."""
    if counts is None:

        counts = {}
        for word in word_list:
            w = word.lower()
            counts[w] = 0 if w not in counts else counts[w]
        word_list = [w.lower() for w in word_list]

    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {
        'User-Agent': 'python:keyword.counter:v1.0 (by /u/yourusername)'}
    params = {'limit': 100}
    if after:
        params['after'] = after

    try:
        response = requests.get(url, headers=headers,
                                params=params, allow_redirects=False)
        if response.status_code != 200:
            return
        data = response.json()
    except Exception:
        return

    posts = data.get('data', {}).get('children', [])
    for post in posts:
        title = post.get('data', {}).get('title', '').lower()

        words = re.findall(r'\b\w+\b', title)
        for w in word_list:
            counts[w] += words.count(w)

    after = data.get('data', {}).get('after')
    if after:
        count_words(subreddit, word_list, after, counts)
    else:

        filtered = [(word, count)
                    for word, count in counts.items() if count > 0]

        filtered.sort(key=lambda x: (-x[1], x[0]))
        for word, count in filtered:
            print(f"{word}: {count}")
