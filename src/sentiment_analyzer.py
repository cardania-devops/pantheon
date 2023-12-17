import openai

class SentimentAnalyzer:
    def __init__(self, openai_api_key):
        self.openai_api_key = openai_api_key

    def analyze_sentiment(self, text):
        openai.api_key = self.openai_api_key
        try:
            response = openai.Completion.create(
                engine="gpt-3.5-turbo-0613",  # Updated model
                prompt=f"Analyze the sentiment of the following text:\n\n\"{text}\"\n\nSentiment:",
                max_tokens=1,
                n=1,
                stop=None,
                temperature=0.7,
            )
            sentiment = response.choices[0].text.strip()
            return sentiment
        except Exception as e:
            logging.error(f"Error in sentiment analysis: {e}")
            return "Error"
