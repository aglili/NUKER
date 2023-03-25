import tweepy
import time
import re
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.environ.get("api_key")
api_secret_key = os.environ.get("api_secret_key")
client_key = os.environ.get("client_key")
client_secret = os.environ.get("client_secret")
bearer_token= os.environ.get("bearer_token")


auth = tweepy.OAuthHandler(api_key, api_secret_key)
auth.set_access_token(client_key, client_secret)

client = tweepy.Client(consumer_key=api_key,consumer_secret=api_secret_key,access_token=client_key,access_token_secret=client_secret,bearer_token=bearer_token)

def get_tweet_id():
    print("""  .-----------------. .----------------.  .----------------.  .----------------.  .----
| .--------------. || .--------------. || .--------------. || .--------------. || .--------------. |
| | ____  _____  | || | _____  _____ | || |  ___  ____   | || |  _________   | || |  _______     | |
| ||_   \|_   _| | || ||_   _||_   _|| || | |_  ||_  _|  | || | |_   ___  |  | || | |_   __ \    | |
| |  |   \ | |   | || |  | |    | |  | || |   | |_/ /    | || |   | |_  \_|  | || |   | |__) |   | |
| |  | |\ \| |   | || |  | '    ' |  | || |   |  __'.    | || |   |  _|  _   | || |   |  __ /    | |
| | _| |_\   |_  | || |   \ `--' /   | || |  _| |  \ \_  | || |  _| |___/ |  | || |  _| |  \ \_  | |
| ||_____|\____| | || |    `.__.'    | || | |____||____| | || | |_________|  | || | |____| |___| | |
| |              | || |              | || |              | || |              | || |              | |
| '--------------' || '--------------' || '--------------' || '--------------' || '--------------' |
 '----------------'  '----------------'  '----------------'  '----------------'  '----------------'   BY CECILCODESPYTHON""")
    try:
        getUrl = input("Enter the tweet url: ")
        tweet_id = re.search(r'/status/(\d+)', getUrl).group(1)
    except AttributeError:
        print("You entered an incorrect URL. Try Again! ")
    return tweet_id

likers = tweepy.Client.get_liking_users(client,id=get_tweet_id())
user_ids = [user.id for user in likers.data]

no_blocked = len(user_ids)


print("Starting Nuclear Machine")
for user_id in user_ids:
    print(f"blocking user:{user_id}")
    tweepy.Client.block(client,target_user_id=user_id)
    time.sleep(5)

print("The tweet has been nuked")
print(f"{no_blocked} users have been blocked")