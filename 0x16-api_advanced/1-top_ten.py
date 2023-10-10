#!/usr/bin/python3
"""This module is in charge of making the connection with the api and prints
    the titles of the first 10 hot posts listed for a given subreddit."""
import requests


def top_ten(subreddit):
    """This method prints the titles of the first 10 hot posts listed
        for a given subreddit."""
    headers = {"user-agent": "Python3"}
    url = "https://www.reddit.com"
    r = requests.get(f'{url}/r/{redreddit}/hot.json?limit=10', headers=headers)
    if r.status_code != 200:
        print(None)
        return
    for child in r.json().get("data").get("children")[:10]:
        print(child.get("data").get("title"))
