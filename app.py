from flask import Flask, render_template, request, jsonify
import logging
import os
from src.twitter_api import TwitterAPI  # Ensure this path is correct
from src.sentiment_analyzer import SentimentAnalyzer  # Ensure this path is correct
from src.discord_bot import YourDiscordBotClass  # Ensure this path is correct

# Setup advanced logging
logging.basicConfig(filename='app.log', level=logging.INFO, 
                    format='%(asctime)s:%(levelname)s:%(message)s')


# Initialize Flask application
app = Flask(__name__)

# Fetch API keys from environment variables
twitter_api_key = os.getenv('TWITTER_API_KEY')
twitter_api_secret_key = os.getenv('TWITTER_API_SECRET_KEY')
twitter_access_token = os.getenv('TWITTER_ACCESS_TOKEN')
twitter_access_token_secret = os.getenv('TWITTER_ACCESS_TOKEN_SECRET')
openai_api_key = os.getenv('OPENAI_API_KEY')
discord_bot_token = os.getenv('DISCORD_BOT_TOKEN')

try:
    # Initialize TwitterAPI, SentimentAnalyzer, and DiscordBot with the environment variables
    twitter_api = TwitterAPI(api_key=twitter_api_key, api_secret_key=twitter_api_secret_key,
                             access_token=twitter_access_token, access_token_secret=twitter_access_token_secret)
    sentiment_analyzer = SentimentAnalyzer(openai_api_key)
    discord_bot = YourDiscordBotClass(discord_bot_token)  # Initialize with correct class and parameters
except Exception as e:
    logging.error(f"Error in initializing components: {e}")
    raise

@app.route('/')
def index():
    # Home page route
    try:
        # Logic for home page
        return render_template('index.html')
    except Exception as e:
        logging.error(f"Error in home route: {e}")
        return jsonify(error=str(e)), 500

# Additional routes here...

if __name__ == '__main__':
    app.run(debug=True)  # Set debug to False in production
