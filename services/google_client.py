import gspread
from google.oauth2.service_account import Credentials

# Access Scope
SCOPES = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive"
]

# Path [Private]
SERVICE_ACCOUNT_FILE = "credentials/service_account.json"

def get_gspread_client():
    """ 
    Initialize and return an authorized gspread client 
    """
    Credentials = Credentials.from_service_account_file(
    SERVICE_ACCOUNT_FILE , scopes = SCOPES
)
    client = gspread.authorize(Credentials)
    return client