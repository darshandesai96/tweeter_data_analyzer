import oauth2 as oauth
import json
import  matplotlib as plt
from tweepy.streaming import StreamListener
from tweepy import Stream
from tweepy import API
from tweepy import Cursor
from tweepy import OAuthHandler
from tweepy import cursor
import numpy as np
import pandas as pd
import csv

icounter = 0

with open('config1.json') as file:
    tokens = json.loads(file.read())

consumer = oauth.Consumer(key= tokens['CONSUMER_KEY'], secret=tokens['CONSUMER_SECRET'])
token = oauth.Token(key= tokens['ACCESS_TOKEN'], secret= tokens['ACCESS_SECRET'])
client = oauth.Client(consumer,token)



FOLLOWRS_URL = 'https://api.twitter.com/1.1/followers/list.json'

screen_name = '07darshan'

url = FOLLOWRS_URL+'?screen_name='+screen_name

header, response = client.request(url,method='GET')

#print('status:',header['status'])
#return 200 means successful to connect twitter api

class twitter_data():
    def __init__(self):
        self.auth = TwitterAuthenticate().authenticate_twitter()
        self.twitter_client = API(self.auth)

    def get_tweets(self, num_tweets):
      self.auth = TwitterAuthenticate().authenticate_twitter()
      api = API(self.auth)
      '''for tweet in Cursor(api.user_timeline, screen_name="@saheel21",count=100).items(num_tweets):
        print(tweet.created_at, tweet.id ,tweet.user.screen_name, tweet.text,tweet.favorite_count,tweet.retweet_count, tweet.user.location, tweet.entities['hashtags'])
        with open("tweets.csv",'a+',encoding='utf-8') as file:
          f2 = csv.writer(file)
          
          f2.writerow([tweet.id, tweet.created_at, tweet.user.screen_name ,tweet.text.encode('utf-8'),tweet.favorite_count,tweet.retweet_count, tweet.user.location, tweet.entities['hashtags']])'''

      for tweet in Cursor(api.search, q="#tesla",count=100, lang="en", geocode= '39.8098600,-98.5551830,1500km').items(num_tweets):
        tweet.text = evaluateText(tweet.text)
        tweet.entities['hashtags'] = arrangeHashtags(tweet.entities['hashtags'])
        print(tweet.created_at, tweet.id ,tweet.user.screen_name, tweet.text,tweet.favorite_count,tweet.retweet_count, tweet.user.location, tweet.entities['hashtags'])
        with open("twitter.csv",'a+',encoding='utf-8') as file:
          f2 = csv.writer(file)
          f2.writerow([tweet.id, tweet.created_at, tweet.user.screen_name ,tweet.text.encode('utf-8'),tweet.favorite_count,tweet.retweet_count, tweet.user.location, tweet.entities['hashtags']])

class TwitterAuthenticate():
    def authenticate_twitter(self):
        auth = OAuthHandler(consumer_key=tokens['CONSUMER_KEY'], consumer_secret=tokens['CONSUMER_SECRET'])
        auth.set_access_token(key=tokens['ACCESS_TOKEN'], secret=tokens['ACCESS_SECRET'])
        return auth

if __name__ == "__main__":
    icounter = 0
    twitter_client = twitter_data()
    api = twitter_client.get_tweets(500)
