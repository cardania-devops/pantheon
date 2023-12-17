# Collect and preprocess tweets
from twitter_api import TwitterAPI
import os
from .database_manager import DatabaseManager
creds_path = os.getenv('GOOGLE_SHEETS_CREDENTIALS_PATH')
class DataCollector:
    def __init__(self):
        api_key = os.getenv("TWITTER_API_KEY")
        api_secret_key = os.getenv("TWITTER_API_SECRET_KEY")
        access_token = os.getenv("TWITTER_ACCESS_TOKEN")
        access_token_secret = os.getenv("TWITTER_ACCESS_TOKEN_SECRET")

        self.twitter_api = TwitterAPI(api_key, api_secret_key, access_token, access_token_secret)

    def collect_tweets(self, cashtag, count=100):
        # Fetch tweets with the cashtag
        tweets = self.twitter_api.fetch_tweets_with_cashtag(cashtag, count)
        # Here, you can add additional processing or filtering of tweets if necessary
        return tweets
    def save_to_sheet(self, processed_data):
        db_manager = DatabaseManager('path/to/your/credentials.json', 'Argus Sheet Name')
        for data in processed_data:
            db_manager.save_data(data)        

# Example usage:
collector = DataCollector()
tweets = collector.collect_tweets("BTC", 10)
for tweet in tweets:
    print(tweet)
