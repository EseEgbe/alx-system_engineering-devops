#!/usr/bin/python3
"""
Function that queries the Reddit API and returns
the number of subscribers for a given subreddit.
"""
import requests

def number_of_subscribers(subreddit):
    """ Queries to Reddit API """
    headers = {'User-Agent': 'CustomUserAgent/1.0'}
    url = f'https://www.reddit.com/r/{subreddit}/about.json'
    response = requests.get(url, headers=headers, allow_redirects=False)
    
    if response.status_code == 200:
        return response.json()['data']['subscribers']
    else:
        return 0
