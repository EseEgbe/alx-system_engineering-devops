#!/usr/bin/python3
"""Function to print hot posts on a given Reddit subreddit."""
import requests

def top_ten(subreddit):
    url = f'https://www.reddit.com/r/{subreddit}/hot.json'
    headers = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"
    }
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code != 200:
        print(None)
        return

    posts = response.json().get('data', {}).get('children', [])
    for post in posts[:10]:
        print(post['data']['title'])
