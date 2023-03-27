import praw
import os
from dotenv import load_dotenv
load_dotenv()

reddit=praw.Reddit(client_id=os.getenv('client_id'),client_secret=os.getenv('client_secret'),username='hegdeshreyas',password=os.getenv('password'),user_agent='prawtutorial')


hot_posts = reddit.subreddit('MachineLearning').new(limit=10)
print(hot_posts)
for post in hot_posts:
    print(post.title)
