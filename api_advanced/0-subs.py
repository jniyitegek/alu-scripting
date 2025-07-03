#!/usr/bin/python3
"""This module provides using the Reddit public API."""
import requests


def number_of_subscribers(subreddit):
    """
    Return the number of subscribers for a given subreddit.
    
    Args:
        subreddit (str): The name of the subreddit (without 'r/' prefix).
        
    Returns:
        int: Number of subscribers, or 0 if subreddit doesn't exist or an error occurs.
    """
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