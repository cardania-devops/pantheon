from flask import Flask, render_template, request
import logging
import os
from src.twitter_api import TwitterAPI  # Updated import path
from src.sentiment_analyzer import SentimentAnalyzer  # Updated import path
from src.discord_bot import YourDiscordBotClass  # Ensure this path is correct

# Initialize Flask application
app = Flask(__name__)

# Fetch API keys from environment variables
twitter_api_key = os.getenv('TWITTER_API_KEY')
twitter_api_secret_key = os.getenv('TWITTER_API_SECRET_KEY')
twitter_access_token = os.getenv('TWITTER_ACCESS_TOKEN')
twitter_access_token_secret = os.getenv('TWITTER_ACCESS_TOKEN_SECRET')
openai_api_key = os.getenv('OPENAI_API_KEY')
discord_bot_token = os.getenv('DISCORD_BOT_TOKEN')

# Initialize TwitterAPI, SentimentAnalyzer, and DiscordBot with the environment variables
twitter_api = TwitterAPI(
    api_key=twitter_api_key,
    api_secret_key=twitter_api_secret_key,
    access_token=twitter_access_token,
    access_token_secret=twitter_access_token_secret
)
sentiment_analyzer = SentimentAnalyzer(openai_api_key)
discord_bot = YourDiscordBotClass(discord_bot_token)  # Initialize your Discord bot

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    if request.method == 'POST':
        cashtag = request.form['cashtag']
        try:
            tweets = twitter_api.fetch_tweets_with_cashtag(cashtag, count=10)
            sentiments = [sentiment_analyzer.analyze_sentiment(tweet) for tweet in tweets]
            results = f"Sentiments for {cashtag}: " + ', '.join(sentiments)
        except Exception as e:
            logging.error(f"Error in analyzing sentiment for {cashtag}: {e}")
            results = "An error occurred while analyzing."
        return render_template('results.html', results=results)

if __name__ == '__main__':
    app.run(debug=True)
