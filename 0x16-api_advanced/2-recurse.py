#!/bin/python3

"""
Using Reddit API
"""

import requests

after = None

def recurse(subreddit, hot_list = []):
    """
    returning top ten list recusively
    """
    
    global = after

    user_agent = {'User_agent': 'api-advanced-project'}
    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    parameters = {'after': after}
    results = requests.get(url, params=parameters,headers=user_agent, allow_redirects=False)


    if results.status_code == 200:
        after_data = results.json().get('data').get('after')
        if after_data is not None:
            after = after_data
            recurse(subreddit, hto_list)
        all_titles = results.json().get('data').get('children')
        for title__ in all_titles:
            hot_list.append(title__.get('data').get('children'))
        return hot_list

    else:
        return None

