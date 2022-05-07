from ast import keyword
# from numpy import result_type for search result i.e-mixed, latest, etc
import tweepy
import keys
import time, datetime

auth = tweepy.OAuthHandler(keys.API_KEY, keys.API_SECRET_KEY)
auth.set_access_token(keys.ACCESS_TOKEN, keys.SECRET_ACCESS_TOKEN)
api = tweepy.API(auth, wait_on_rate_limit=True)

def twitter_bot(Keywords, delay):
  while True:
    print(f"\n{datetime.datetime.now()}\n")

    for tweets in tweepy.Cursor(api.search_tweets, q=Keywords, count=5).items(5):
      try:
        tweet_id = dict(tweets._json)["id"]
        tweet_text = dict(tweets._json)["text"]

        print("id: " + str(tweet_id))
        print("text: " + str(tweet_text))

        api.retweet(tweet_id)

      except:print("Error")

    time.sleep(delay)

twitter_bot("मिथिला", 351)


