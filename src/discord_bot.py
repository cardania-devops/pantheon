import discord
import logging
from discord.ext import commands
from os import getenv
from twitter_api import TwitterAPI
from sentiment_analyzer import SentimentAnalyzer
from market_analyzer import MarketAnalyzer
from signal_generator import SignalGenerator

# Initialize logging
logging.basicConfig(level=logging.INFO, 
                    filename='bot.log', 
                    filemode='a', 
                    format='%(asctime)s - %(levelname)s - %(name)s: %(message)s')

class CustomHelpCommand(commands.HelpCommand):
    # ... existing CustomHelpCommand methods ...

class SignalBot(commands.Bot):
    def __init__(self, command_prefix):
        intents = discord.Intents.default()
        super().__init__(command_prefix=command_prefix, intents=intents, help_command=CustomHelpCommand())
        self.twitter_api = TwitterAPI()  # Initialize the TwitterAPI
        self.sentiment_analyzer = SentimentAnalyzer()  # Initialize the SentimentAnalyzer
        self.market_analyzer = MarketAnalyzer()  # Initialize the MarketAnalyzer
        self.signal_generator = SignalGenerator()  # Initialize the SignalGenerator

    async def on_ready(self):
        logging.info(f"{self.user} has connected to Discord!")

    @commands.command(name='analyze', help='Analyzes the given cashtag')
    async def analyze(self, ctx, cashtag: str):
        try:
            # Logic to fetch data from Twitter based on cashtag
            tweets = self.twitter_api.fetch_tweets_with_cashtag(cashtag)
            # Analyze sentiment
            sentiments = [self.sentiment_analyzer.analyze_sentiment(tweet) for tweet in tweets]
            # Process and respond
            response = "Analysis complete."
        except Exception as e:
            logging.error(f"Error in analyze command: {str(e)}")
            response = f"An error occurred: {str(e)}"
        await ctx.send(response)

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
