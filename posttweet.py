# importing the module
import tweepy
import keys

  
# authentication of consumer key and secret
auth = tweepy.OAuthHandler(keys.API_KEY, keys.API_SECRET_KEY)
  
# authentication of access token and secret
auth.set_access_token(keys.ACCESS_TOKEN, keys.SECRET_ACCESS_TOKEN)
api = tweepy.API(auth, wait_on_rate_limit=True)
  
# update the status
api.update_status(status ="Hello...!!!")
