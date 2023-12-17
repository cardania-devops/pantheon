import requests
import os

class MarketAnalyzer:
    def __init__(self):
        self.base_url = os.getenv("MARKET_API_BASE_URL")

    def fetch_current_price(self, token):
        try:
            response = requests.get(f"{self.base_url}/current_price/{token}")
            response.raise_for_status()  # Raises a HTTPError if the HTTP request returned an unsuccessful status code
            return response.json()
        except requests.RequestException as e:
            print(f"Error fetching current price: {e}")
            return None

    def fetch_historical_data(self, token, start_date, end_date):
        try:
            response = requests.get(f"{self.base_url}/historical_data/{token}?start={start_date}&end={end_date}")
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            print(f"Error fetching historical data: {e}")
            return None

# Example usage
analyzer = MarketAnalyzer()
current_price = analyzer.fetch_current_price("BTC")
historical_data = analyzer.fetch_historical_data("BTC", "2023-01-01", "2023-01-31")
