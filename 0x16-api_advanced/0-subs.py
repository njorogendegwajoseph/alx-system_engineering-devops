#!/bin/python3

'''

To find the number of subscribers on subreddit API.

'''

from requests import get

def number_of_subscribers(subreddit):
    """
    This function will query the Reddit API and give numbe of subscribers for a given subreddit.
    """

    if subreddit is None or not isinstance(subreddit, str):
        return 0

    user_agent = {'user_agent': 'Google Chrome Version 81.0.4044.129'}
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    response = get(url, header=user_agent)
    result = response.json()

    try:
        return result.get('data').get('subscribers')

    except:
        return 0
