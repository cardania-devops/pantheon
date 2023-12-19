# Collect and preprocess tweets
from .twitter_api import TwitterAPI
import os
import logging
from .database_manager import DatabaseManager

# Setup basic logging
logging.basicConfig(level=logging.INFO)

class DataCollector:
    def __init__(self):
        api_key = os.getenv("TWITTER_API_KEY")
        api_secret_key = os.getenv("TWITTER_API_SECRET_KEY")
        access_token = os.getenv("TWITTER_ACCESS_TOKEN")
        access_token_secret = os.getenv("TWITTER_ACCESS_TOKEN_SECRET")

        self.twitter_api = TwitterAPI(api_key, api_secret_key, access_token, access_token_secret)

    def collect_tweets(self, cashtag, count=100):
        try:
            # Fetch tweets with the cashtag
            tweets = self.twitter_api.fetch_tweets_with_cashtag(cashtag, count)
            # Additional processing or filtering of tweets can be added here
            return tweets
        except Exception as e:
            logging.error(f"Error in collecting tweets: {e}")
            return []

    def save_to_sheet(self, processed_data):
        creds_path = os.getenv('GOOGLE_SHEETS_CREDENTIALS_PATH', 'path/to/your/credentials.json')
        db_manager = DatabaseManager(creds_path, 'Argus Sheet Name')
        try:
            for data in processed_data:
                db_manager.save_data(data)
        except Exception as e:
            logging.error(f"Error in saving data to sheet: {e}")

# Example usage:
if __name__ == "__main__":
    collector = DataCollector()
    tweets = collector.collect_tweets("BTC", 10)
    for tweet in tweets:
        print(tweet)
