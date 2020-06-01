import tweepy
import time

auth = tweepy.OAuthHandler('xxxx','xxxx')
auth.set_access_token('xxxx','xxxx')

api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

user = api.me()

search = '#x'
nrTweets = 500

for tweet in tweepy.Cursor(api.search, search).items(nrTweets):
    try:
        print('Liked tweet')
        tweet.favorite()
        time.sleep(10)
    except tweepy.TweepError as e:
        print(e.reason)
    except StopIteration:
        break 