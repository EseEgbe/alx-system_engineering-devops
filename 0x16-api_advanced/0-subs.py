#!/usr/bin/python3
"""
Function that queries the Reddit API and returns
the number of subscribers for a given subreddit.
"""
import requests

def number_of_subscribers(subreddit):
    """ Queries to Reddit API """
    custom_user_agent = 'Mozilla/5.0'

    headers = {
        'User-Agent':custom_ user_agent
    }

    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    response = requests.get(url, headers=headers, allow_redirects=False)
    
    if response.status_code == 200:
        return response.json()['data']['subscribers']
    else:
        return 0

