# Configuration variables and API keys
import os

# Configuration for Twitter API (Using Environment Variables)
TWITTER_API_KEY = os.getenv('TWITTER_API_KEY')
TWITTER_API_SECRET_KEY = os.getenv('TWITTER_API_SECRET_KEY')
TWITTER_ACCESS_TOKEN = os.getenv('TWITTER_ACCESS_TOKEN')
TWITTER_ACCESS_TOKEN_SECRET = os.getenv('TWITTER_ACCESS_TOKEN_SECRET')

# Configuration for Sentiment Analysis
SENTIMENT_ANALYSIS_MODEL = 'gpt-4-1106-preview'  # Model used for sentiment analysis

# Other configuration parameters can be added here
