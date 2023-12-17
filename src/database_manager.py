import gspread
import os
from oauth2client.service_account import ServiceAccountCredentials

class DatabaseManager:
    def __init__(self, sheet_name):
        creds_path = os.getenv('GOOGLE_SHEETS_CREDENTIALS_PATH')
        scope = [
            "https://spreadsheets.google.com/feeds",
            'https://www.googleapis.com/auth/spreadsheets',
            "https://www.googleapis.com/auth/drive.file",
            "https://www.googleapis.com/auth/drive"
        ]
        creds = ServiceAccountCredentials.from_json_keyfile_name(creds_path, scope)
        client = gspread.authorize(creds)
        self.sheet = client.open(sheet_name).sheet1  # Open the first sheet

    def save_data(self, data):
        self.sheet.append_row(data)

    def get_all_data(self):
        return self.sheet.get_all_records()
