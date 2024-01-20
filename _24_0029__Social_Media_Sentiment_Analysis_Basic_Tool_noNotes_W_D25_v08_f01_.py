import tweepy
from textblob import TextBlob
import pandas as pd

consumer_key = 'YOUR_CONSUMER_KEY'
consumer_secret = 'YOUR_CONSUMER_SECRET'
access_token = 'YOUR_ACCESS_TOKEN'
access_token_secret = 'YOUR_ACCESS_TOKEN_SECRET'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

def fetch_tweets(keyword, count=100):
    tweets = tweepy.Cursor(api.search_tweets, q=keyword, lang="en").items(count)
    return [tweet.text for tweet in tweets]

def analyze_sentiments(tweets):
    sentiments = {'positive': 0, 'neutral': 0, 'negative': 0}
    for tweet in tweets:
        analysis = TextBlob(tweet)
        if analysis.sentiment.polarity > 0:
            sentiments['positive'] += 1
        elif analysis.sentiment.polarity == 0:
            sentiments['neutral'] += 1
        else:
            sentiments['negative'] += 1
    return sentiments

def main():
    keyword = input("Enter keyword to analyze: ")
    tweets = fetch_tweets(keyword)
    sentiments = analyze_sentiments(tweets)
    print(f"Sentiment Analysis for '{keyword}':")
    for sentiment, count in sentiments.items():
        print(f"{sentiment.capitalize()}: {count}")

if __name__ == "__main__":
    main()
