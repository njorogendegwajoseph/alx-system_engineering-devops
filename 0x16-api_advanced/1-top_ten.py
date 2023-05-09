#!/bin/python3

"""
This should print the title of the first ten hot posts listed for a subreddit
"""

form requests import get

def top_ten(subreddit):
    """
    This function querries the reddit API and gives the top ten subreddit, prints the title.

    """

    if subreddit is None or not isinstance(subreddit, str):
    return 0

    user_agent = {'User_agent': 'Google Chrome Version 81.0.4044.129'}
    params = {'limit': 10}
    url = 'https://reddit.com/r/hot/.json'.format(subreddit)

    response = get(url, headers = user_agent, params=params)
    results = response.json()


    try:
        the_data = results.get('data').get('children')

        for i in the_data:
            print(i.get('data').get('title'))

    except:
        print('None')
