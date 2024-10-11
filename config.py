import os

#Bot token @Botfather
BOT_TOKEN = os.environ.get("BOT_TOKEN", "")

#Your API ID from my.telegram.org
API_ID = int(os.environ.get("API_ID", "16214694"))

#Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "7545825d90eb7adae543d59909c73121")

#Database 
DB_URI = os.environ.get("DB_URI", "mongodb+srv://sandisir741:K4pXJjQy0d4uIM9s@cluster0.qnqye.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
