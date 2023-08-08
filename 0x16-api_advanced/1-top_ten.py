def top_ten(subreddit):
    user_agent = "Mozilla/5.0 (X11; Linux x86_64; rv:102.0) Gecko/20100101 Firefox/102.0"  
    headers = {"User-Agent": user_agent}
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    
    response = requests.get(url, headers=headers, allow_redirects=False)
    
    if response.status_code == 200:
        try:
            data = response.json()
            posts = data["data"]["children"]
            for post in posts:
                title = post["data"]["title"]
                print(title)
        except (KeyError, ValueError):
            print("An error occurred while fetching data.")
    else:
        print("Invalid subreddit or an error occurred.")