import os

# Bot token @Botfather
BOT_TOKEN = os.environ.get("BOT_TOKEN", "")

# Your API ID from my.telegram.org
API_ID = int(os.environ.get("API_ID", "29968201"))

# Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "a6b9ce1c391c28b896705716e4755821")

# Your Owner / Admin Id For Broadcast 
ADMINS = int(os.environ.get("ADMINS", "974746927"))

# Your Mongodb Database Url
DB_URI = os.environ.get("DB_URI", "mongodb+srv://downloadhdhindimovie:AEu8qkpUtQKXQpxa@cluster0.ufduv.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
DB_NAME = os.environ.get("DB_NAME", "vjsavecontentbot")

# If You Want Error Message In Your Personal Message Then Turn It True Else If You Don't Want Then Flase
ERROR_MESSAGE = bool(os.environ.get('ERROR_MESSAGE', True))
