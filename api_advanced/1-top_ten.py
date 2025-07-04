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
        'User-Agent': 'python:reddit-scraper:v1.0.0 (by /u/testuser)'
    }
    subreddit_url = "https://old.reddit.com/r/{}.json".format(subreddit)
    
    try:
        # Prevent redirects to ensure we're not getting search results
        response = requests.get(subreddit_url, headers=headers, allow_redirects=False, timeout=10)
        
        # Check if the request was successful and not redirected
        if response.status_code == 200:
            try:
                json_data = response.json()
                
                # Verify we have the expected JSON structure
                if (json_data and 
                    'data' in json_data and 
                    'children' in json_data['data'] and
                    isinstance(json_data['data']['children'], list)):
                    
                    children = json_data['data']['children']
                    
                    # Print up to 10 post titles (or fewer if less than 10 posts exist)
                    count = 0
                    for i in range(min(10, len(children))):
                        if 'data' in children[i] and 'title' in children[i]['data']:
                            title = children[i]['data']['title']
                            if title:  # Only print non-empty titles
                                print(title)
                                count += 1
                    
                    # If we didn't print any titles, it's an invalid subreddit
                    if count == 0:
                        print(None)
                        
                else:
                    print(None)
                    
            except (ValueError, KeyError, TypeError):
                print(None)
        else:
            # Any non-200 status code (including redirects) means invalid subreddit
            print(None)
            
    except requests.RequestException:
        # Handle network errors
        print(None)
