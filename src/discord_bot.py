import discord
import logging
from os import getenv
from .twitter_api import TwitterAPI
from .sentiment_analyzer import SentimentAnalyzer
from .market_analyzer import MarketAnalyzer
from .signal_generator import SignalGenerator
from discord.ext import commands
import json

# Initialize logging
logging.basicConfig(level=logging.INFO,
                    filename='bot.log',
                    filemode='a',
                    format='%(asctime)s - %(levelname)s - %(name)s: %(message)s')

class CustomHelpCommand(commands.HelpCommand):
    pass  # Replace with your CustomHelpCommand methods

class SignalBot(commands.Bot):
    def __init__(self, command_prefix):
        super().__init__(command_prefix=command_prefix, intents=discord.Intents.default(), help_command=CustomHelpCommand())
        
        twitter_api_key = getenv('TWITTER_API_KEY')
        twitter_api_secret_key = getenv('TWITTER_API_SECRET_KEY')
        twitter_access_token = getenv('TWITTER_ACCESS_TOKEN')
        twitter_access_token_secret = getenv('TWITTER_ACCESS_TOKEN_SECRET')

        self.twitter_api = TwitterAPI(api_key=twitter_api_key,
                                      api_secret_key=twitter_api_secret_key,
                                      access_token=twitter_access_token,
                                      access_token_secret=twitter_access_token_secret)
        self.sentiment_analyzer = SentimentAnalyzer(getenv('OPENAI_API_KEY'))
        # Initialize other components if necessary

    async def on_ready(self):
        logging.info(f"{self.user} has connected to Discord!")

    @commands.command(name='analyze', help='Analyzes the given cashtag')
    async def analyze(self, ctx, cashtag: str):
        try:
            tweets = self.twitter_api.fetch_tweets_with_cashtag(cashtag)
            sentiments = [self.sentiment_analyzer.analyze_sentiment(tweet) for tweet in tweets]
            response = "Analysis complete. Use the 'results' command to view the analysis."
        except Exception as e:
            logging.error(f"Error in analyze command: {str(e)}")
            response = f"An error occurred: {str(e)}"
        await ctx.send(response)

    @commands.command(name='results', help='Displays the results of the last analysis')
    async def display_results(self, ctx):
        try:
            with open('results.json', 'r') as file:
                data = json.load(file)
            message = f"Analysis for {data['cashtag']}:\n" + '\n'.join(data['sentiments'])
            await ctx.send(message)
        except Exception as e:
            await ctx.send(f"Error retrieving results: {e}")

    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.CommandError):
            logging.error(f"Command error in {ctx.command}: {error}")
            await ctx.send(f"An error occurred: {error}")

if __name__ == "__main__":
    token = getenv("DISCORD_BOT_TOKEN")
    if not token:
        raise ValueError("DISCORD_BOT_TOKEN environment variable not set")
    bot = SignalBot(command_prefix="!")
    bot.run(token)
