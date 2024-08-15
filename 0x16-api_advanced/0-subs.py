#!/usr/bin/python3
'''A module containing functions for working with the Reddit API.
'''
import requests

BASE_URL = 'https://www.reddit.com'
'''Reddit's base API URL.
'''

def number_of_subscribers(subreddit):
    '''Retrieves the number of subscribers in a given subreddit.
    '''
    
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {'User-Agent': 'Mozilla/5.0'}
    response = requests.get(url, headers=headers, allow_redirects=False)
    
    if response.status_code == 200:
        data = response.json()
        return data['data']['subscribers']
    else:
        return 0
