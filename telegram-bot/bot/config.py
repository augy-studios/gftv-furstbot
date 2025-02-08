import os
from dotenv import load_dotenv

# Load all variables from token.env
load_dotenv("token.env")

API_ID = os.getenv("API_ID")
API_HASH = os.getenv("API_HASH")
BOT_TOKEN = os.getenv("BOT_TOKEN")
LOG_CHANNEL_ID = int(os.getenv("LOG_CHANNEL_ID")) if os.getenv("LOG_CHANNEL_ID") else None
BOT_OWNER_ID = int(os.getenv("BOT_OWNER_ID")) if os.getenv("BOT_OWNER_ID") else None

SHEET_URL = str(os.getenv("SHEET_URL")) if os.getenv("SHEET_URL") else None
SHEET_HELLO = str(os.getenv("SHEET_HELLO")) if os.getenv("SHEET_HELLO") else None
SHEET_2025 = str(os.getenv("SHEET_2025")) if os.getenv("SHEET_2025") else None
