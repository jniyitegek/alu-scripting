#!/usr/bin/python3
"""Print the titles of the first 10 hot posts for a given subreddit."""
import requests

def top_ten(subreddit):
    """Print the titles of the first 10 hot posts for a given subreddit."""
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {'User-Agent': 'Python:top_ten:v1.0 (by /u/yourusername)'}
    params = {'limit': 10}
    try:
        response = requests.get(url, headers=headers,
                                params=params, allow_redirects=False)
        if response.status_code != 200:
            print(None)
            return
        data = response.json()
        posts = data.get('data', {}).get('children', [])
        for post in posts:
            print(post.get('data', {}).get('title'))
    except Exception:
        print(None)
