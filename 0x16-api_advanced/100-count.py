#!/usr/bin/python3
"""This module is in charge of making the connection with the
    api and parses the title of all hot articles, and prints a
    sorted count of given keywords."""
import requests


def recurse(subreddit, hot_list=[], after=""):
    """This method returns a list containing the titles of all
        hot articles for a given subreddit"""
    headers = {"user-agent": "1637-holberton"}
    if after is None:
        return hot_list
    if after == "":
        r = requests.get('https://www.reddit.com/r/{}/hot.json'.format(
            subreddit), headers=headers, allow_redirects=False)
    else:
        r = requests.get(
            'https://www.reddit.com/r/{}/hot.json?after={}'.format(
                subreddit, after), headers=headers, allow_redirects=False)
    if r.status_code != 200:
        return None
    after = r.json().get("data").get("after")
    for child in r.json().get("data").get("children"):
        hot_list.append(child.get("data").get("title"))
    return recurse(subreddit, hot_list, after)


def count_words(subreddit, word_list):
    """This method parses the title of all hot articles,
        and prints a sorted count of given keywords."""
    ts = recurse(subreddit)
    if ts is None:
        return
    list_all = []
    for w in word_list:
        all_sum = 0
        for t in ts:
            all_sum += t.lower().split().count(w.lower())
        if all_sum > 0:
            list_all.append([w, all_sum])
    list_all = sorted(list_all, key=lambda x: x[0])
    for k, v in sorted(list_all, key=lambda x: x[1], reverse=True):
        print("{}: {}".format(k, v))
