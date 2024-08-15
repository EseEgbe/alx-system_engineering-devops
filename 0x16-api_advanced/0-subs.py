#!/usr/bin/python3
"""Function to query total subscribers on a Subreddit."""

import requests

def number_of_subscribers(subreddit):
    headers = {'User-Agent': 'Custom User Agent'}
    url = f'https://www.reddit.com/r/{subreddit}/about.json'
    
    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        if response.status_code == 200:
            return response.json()['data']['subscribers']
        else:
            return 0
    except Exception:
        return 0
