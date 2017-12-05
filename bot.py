import markovify

with open('morty.txt', 'r', encoding="ISO-8859-1") as f:
    txt = f.readlines()

text_model = markovify.NewlineText(''.join(txt),state_size=1)

def get_tweet(text_model):
    tweet = text_model.make_short_sentence(140)
    tweet = tweet[0].upper() + tweet[1:]
    return tweet

import tweepy
from time import sleep

consumer_key = 'insert here'
consumer_secret = 'insert here'
access_token = 'insert here'
access_token_secret = 'insert here'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

while True:
    try:
        tweet = get_tweet(text_model)
        api.update_status(tweet)
    except tweepy.TweepError as e:
        print(e.reason)
    sleep(86400)
