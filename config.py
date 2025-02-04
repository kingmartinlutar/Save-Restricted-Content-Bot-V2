# devgagan
# Note if you are trying to deploy on vps then directly fill values in ("")

from os import getenv

API_ID = int(getenv("API_ID", "25444644"))
API_HASH = getenv("API_HASH", "bff60a5f566d9a54c175b0001ba9615b")
BOT_TOKEN = getenv("BOT_TOKEN", "8056263089:AAHMI88zp5GyHzeaQS82BKNzGFzEI_5DAPs")
OWNER_ID = list(map(int, getenv("OWNER_ID", "5969730414").split()))
MONGO_DB = getenv("MONGO_DB", "mongodb+srv://lelouchlightlevi:gZRinZeJNXI55Va0@cluster0.n99js.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
LOG_GROUP = getenv("LOG_GROUP", "")
CHANNEL_ID = int(getenv("CHANNEL_ID", ""))
FREEMIUM_LIMIT = int(getenv("FREEMIUM_LIMIT", "0"))
PREMIUM_LIMIT = int(getenv("PREMIUM_LIMIT", "500"))
WEBSITE_URL = getenv("WEBSITE_URL", "upshrink.com")
AD_API = getenv("AD_API", "")
STRING = getenv("STRING", None)
YT_COOKIES = getenv("YT_COOKIES", None)
INSTA_COOKIES = getenv("INSTA_COOKIES", None)
