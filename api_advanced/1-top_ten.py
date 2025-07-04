#!/usr/bin/python3
"""Script that fetch 10 hot post for a given subreddit."""
import requests


def top_ten(subreddit):
    """Print the titles of the first 10 hot posts for a given subreddit.
    If not a valid subreddit, print None."""
    
    if not subreddit or not isinstance(subreddit, str):
        print(None)
        return
    
    headers = {
        'User-Agent': 'python:MyAPI:v1.0.0 (by /u/testuser)',
        'Accept': 'application/json'
    }
    subreddit_url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    
    try:
        # Prevent redirects to ensure we're not getting search results
        response = requests.get(subreddit_url, headers=headers, allow_redirects=False, timeout=10)
        
        # Check if the request was successful and not redirected
        if response.status_code == 200:
            json_data = response.json()
            
            # Verify we have the expected JSON structure
            if (json_data.get('data') and 
                json_data.get('data').get('children') and
                isinstance(json_data.get('data').get('children'), list)):
                
                children = json_data.get('data').get('children')
                
                # Print up to 10 post titles (or fewer if less than 10 posts exist)
                posts_printed = 0
                for i in range(min(10, len(children))):
                    post_data = children[i].get('data', {})
                    title = post_data.get('title')
                    if title:
                        print(title)
                        posts_printed += 1
                
                # If no posts were printed, print None
                if posts_printed == 0:
                    print(None)
            else:
                print(None)
        else:
            # Any non-200 status code (including redirects) means invalid subreddit
            print(None)
            
    except (requests.RequestException, ValueError, KeyError, AttributeError):
        # Handle network errors, JSON parsing errors, or missing keys
        print(None)
