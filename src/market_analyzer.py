import subprocess
import json
import logging
import os

class MarketAnalyzer:
    # ... existing class methods ...

    def fetch_current_price_from_minswap(self):
        try:
            result = subprocess.run(['node', 'minswap_interface.js', 'getCurrentPrice'],
                                    capture_output=True, text=True, check=True)
            return json.loads(result.stdout)
        except subprocess.CalledProcessError as e:
            logging.error(f"Error fetching current price from Minswap: {e}")
            return None

    def fetch_historical_prices_from_minswap(self):
        try:
            result = subprocess.run(['node', 'minswap_interface.js', 'getHistoricalPrices'],
                                    capture_output=True, text=True, check=True)
            return json.loads(result.stdout)
        except subprocess.CalledProcessError as e:
            logging.error(f"Error fetching historical prices from Minswap: {e}")
            return None

# Example usage
# analyzer = MarketAnalyzer()
# current_price = analyzer.fetch_current_price_from_minswap()
# historical_prices = analyzer.fetch_historical_prices_from_minswap()
