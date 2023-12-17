# Configuration variables and API keys
import os

# Fetch and validate Twitter API credentials
TWITTER_API_KEY = os.getenv('TWITTER_API_KEY', 'default_twitter_api_key')
TWITTER_API_SECRET_KEY = os.getenv('TWITTER_API_SECRET_KEY', 'default_twitter_api_secret_key')
TWITTER_ACCESS_TOKEN = os.getenv('TWITTER_ACCESS_TOKEN', 'default_twitter_access_token')
TWITTER_ACCESS_TOKEN_SECRET = os.getenv('TWITTER_ACCESS_TOKEN_SECRET', 'default_twitter_access_token_secret')

# Ensure that default values are replaced or removed in production

# Model used for sentiment analysis
SENTIMENT_ANALYSIS_MODEL = os.getenv('SENTIMENT_ANALYSIS_MODEL', 'gpt-4-1106-preview')

# Additional configuration parameters can be defined here

# Example of separating development and production configurations
if os.getenv('FLASK_ENV') == 'development':
    # Development-specific configurations
    DEBUG = True
else:
    # Production-specific configurations
    DEBUG = False

# Add more configurations as needed for the application
