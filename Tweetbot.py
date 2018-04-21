#Tweepy is open-sourced library hosted on GitHub and enables 
#Python to communicate with Twitter platform and use its API.
#this code won't work unless you insert correct access token and secret
#AND consumer key and secrets between the double quotes
import tweepy

CONSUMER_KEY = "Enter Token Here"
CONSUMER_SECRET = "Enter Token Here"

ACCESS_TOKEN = "Enter Token Here"
ACCESS_TOKEN_SECRET = "Enter Token Here"

#Verification Process
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)

message1 = "Hi @TheBefikra I am tweetbot"
message2 = "Hi @elonmusk I am tweetbot"
message3 = "Hi @dranzer_blaze I am tweetbot"

s = api.update_status(message1)
s = api.update_status(message2)
s = api.update_status(message3)
