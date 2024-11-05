# devggn
# Note if you are trying to deploy on vps then directly fill values in ("")

from os import getenv

API_ID = int(getenv("API_ID", "22533535"))
API_HASH = getenv("API_HASH", "e42d7ae7aaad687d7d7777709932d590")
BOT_TOKEN = getenv("BOT_TOKEN", "7281976439:AAFNnUh8JO3KuqEsXbzTKDHldfD1Vp_tUAs")
OWNER_ID = list(map(int, getenv("OWNER_ID", "6872258796").split()))
MONGO_DB = getenv("MONGO_DB", "mongodb+srv://2workkhairulikhmal:2wHlUgLv2wEu3kMv@cluster0.ldjgr.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
LOG_GROUP = getenv("LOG_GROUP", "-1002345894188")
CHANNEL_ID = int(getenv("CHANNEL_ID", "-1002483904092"))
