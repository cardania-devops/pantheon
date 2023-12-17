# pantheon
Market Analysis &amp; Bot Suite

## Components

### Argus - Sentiment Analyzer
Argus analyzes social media data to gauge market sentiment. It uses the Twitter API to collect relevant tweets and OpenAI's API for sentiment analysis. It includes a Flask-based web interface for real-time sentiment analysis.

### Hermes1 - Market Analyzer
Hermes1 gathers real-time and historical cryptocurrency price data. It utilizes various APIs to fetch current and historical data for specified cryptocurrencies.

### Morpheus - Signal Interpreter
Morpheus interprets and scores data from Argus and Hermes1. It uses a proprietary formula to analyze this data, stores it in a structured database (Google Sheets), and generates trading signals based on these scores.

### Hermes2 - Signal Bot
Hermes2 is responsible for receiving trading signals from Morpheus and disseminating these signals through a Discord channel, enabling timely and actionable communication.

## Installation
Currently, the Pantheon suite is in development. Installation instructions will be provided as components reach a deployable state.

## Usage
Each component of the Pantheon project will have specific usage instructions detailed in their respective README files.

## Contributing
Contributions to the Pantheon project are welcome. Please refer to our contribution guidelines for more information on how to participate.

## License
None as of this time.

## Additional Project Files
- **`.gitignore`**: Specifies intentionally untracked files to ignore.
- **`config/`**:
  - `config.py`: Contains configuration variables and API keys for each component.
  - `google-credentials.json`: Template for Google Sheets API credentials (actual credentials not tracked in Git).
