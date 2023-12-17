import gspread
import os
import logging
from oauth2client.service_account import ServiceAccountCredentials

# Setup basic logging
logging.basicConfig(level=logging.INFO)

class DatabaseManager:
    def __init__(self, sheet_name, sheet_number=0):
        creds_path = os.getenv('GOOGLE_SHEETS_CREDENTIALS_PATH')
        if not creds_path:
            logging.error("Google Sheets credentials path not found.")
            raise FileNotFoundError("Credentials path not found")

        scope = [
            "https://spreadsheets.google.com/feeds",
            'https://www.googleapis.com/auth/spreadsheets',
            "https://www.googleapis.com/auth/drive.file",
            "https://www.googleapis.com/auth/drive"
        ]
        try:
            creds = ServiceAccountCredentials.from_json_keyfile_name(creds_path, scope)
            client = gspread.authorize(creds)
            self.sheet = client.open(sheet_name).get_worksheet(sheet_number)
            logging.info(f"Connected to Google Sheets: {sheet_name}, Sheet Number: {sheet_number}")
        except Exception as e:
            logging.error(f"Error in Google Sheets connection: {e}")
            raise

    def save_data(self, data):
        try:
            self.sheet.append_row(data)
            logging.info("Data saved successfully.")
        except Exception as e:
            logging.error(f"Error in saving data: {e}")

    def get_all_data(self):
        try:
            data = self.sheet.get_all_records()
            logging.info("Data retrieved successfully.")
            return data
        except Exception as e:
            logging.error(f"Error in retrieving data: {e}")
            return []

# Example usage (if needed for testing or demonstration)
if __name__ == "__main__":
    db_manager = DatabaseManager("Your Sheet Name", sheet_number=1)
    data = db_manager.get_all_data()
    print(data)
