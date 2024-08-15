#!/usr/bin/python3
"""Function to query total subscribers on a given Reddit subreddit."""
import requests

def number_of_subscribers(subreddit):
    """Function to query total subscribers on a given Reddit subreddit."""
    headers = {'User-Agent': 'Mozilla/5.0'}
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    response = requests.get(url, headers=headers, allow_redirects=False)
    
    if response.status_code == 404:
        return 0
    results = response.json().get("data")
    return results.get("subscribers")
