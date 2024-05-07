#!/usr/bin/python3
"""
function that queries the Reddit API and returns
    the number of subscribers
"""

import requests


def number_of_subscribers(subreddit):
"""
function that queries the Reddit API and
returns the number of subscribers
if not a valid subreddit, return 0.
"""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    req = requests.get(url, headers={"User-Agent": "Custom"})

    if req.status_code == 200:
        return req.json().get("data").get("subscribers")
    else:
        return 0
