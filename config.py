import os

#Bot token @Botfather
BOT_TOKEN = os.environ.get("BOT_TOKEN", "")

#Your API ID from my.telegram.org
API_ID = int(os.environ.get("API_ID", "9907234"))

#Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "11b9539664cad67cce0f740c88835cb7")

#Database 
DB_URI = os.environ.get("DB_URI", "mongodb+srv://sandisir741:K4pXJjQy0d4uIM9s@cluster0.qnqye.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
