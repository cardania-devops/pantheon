import tweepy
import time
import os
import logging

# Setup basic logging
logging.basicConfig(level=logging.INFO)

class TwitterAPI:
    def __init__(self, api_key, api_secret_key, access_token, access_token_secret):
        auth = tweepy.OAuthHandler(api_key, api_secret_key)
        auth.set_access_token(access_token, access_token_secret)
        self.api = tweepy.API(auth)
        self.last_call = None

    def _rate_limit(self):
        if self.last_call is not None:
            elapsed = time.time() - self.last_call
            if elapsed < 300:  # 300 seconds = 5 minutes
                time.sleep(300 - elapsed)
        self.last_call = time.time()

    def fetch_tweets_with_cashtag(self, cashtag, count=100):
        self._rate_limit()  # Apply rate limiting
        query = f"${cashtag} -filter:retweets"
        try:
            tweets = self.api.search_tweets(q=query, count=count, tweet_mode='extended')
            return [tweet.full_text for tweet in tweets]
        except Exception as e:
            logging.error(f"Error fetching tweets: {e}")
            return []

# Example usage (if needed for testing or demonstration)
if __name__ == "__main__":
    api_key = os.getenv("TWITTER_API_KEY")
    api_secret_key = os.getenv("TWITTER_API_SECRET_KEY")
    access_token = os.getenv("TWITTER_ACCESS_TOKEN")
    access_token_secret = os.getenv("TWITTER_ACCESS_TOKEN_SECRET")

    twitter_api = TwitterAPI(api_key, api_secret_key, access_token, access_token_secret)
    tweets = twitter_api.fetch_tweets_with_cashtag("BTC", 10)
    for tweet in tweets:
        print(tweet)
