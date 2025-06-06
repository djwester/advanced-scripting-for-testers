import gspread
from google.oauth2.service_account import Credentials

# UPdate to point to your service account file
SERVICE_ACCOUNT_FILE = "../advancedscripting-da4417eb3e72.json"

SCOPES = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive",
]

creds = Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=SCOPES)
client = gspread.authorize(creds)
