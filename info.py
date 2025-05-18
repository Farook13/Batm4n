import re
from os import environ
from flask import Flask
import threading

# Regex to validate numeric IDs
id_pattern = re.compile(r'^.\d+$')

# Converts string to boolean based on common truthy/falsy values
def is_enabled(value, default):
    if value.lower() in ["true", "yes", "1", "enable", "y"]:
        return True
    elif value.lower() in ["false", "no", "0", "disable", "n"]:
        return False
    else:
        return default

# --- Bot Configuration ---
SESSION = environ.get('SESSION', 'Media_search')
API_ID = int(environ.get('API_ID', '12618934'))
API_HASH = environ.get('API_HASH', '49aacd0bc2f8924add29fb02e20c8a16')
BOT_TOKEN = environ.get('BOT_TOKEN', '7693803634:AAFIWfW8gfzMYv-G5-I9hAnge1mYFVkspio')

CACHE_TIME = int(environ.get('CACHE_TIME', 300))
USE_CAPTION_FILTER = bool(environ.get('USE_CAPTION_FILTER', False))

PICS = (environ.get('PICS', 'https://telegra.ph/file/7e56d907542396289fee4.jpg')).split()

ADMINS = [int(admin) if id_pattern.search(admin) else admin for admin in environ.get('ADMINS', '5032034594').split()]
CHANNELS = [int(ch) if id_pattern.search(ch) else ch for ch in environ.get('CHANNELS', '-100247455487').split()]
auth_users = [int(user) if id_pattern.search(user) else user for user in environ.get('AUTH_USERS', '').split()]
AUTH_USERS = (auth_users + ADMINS) if auth_users else []

auth_channel = environ.get('AUTH_CHANNEL')
auth_grp = environ.get('AUTH_GROUP')
AUTH_CHANNEL = int(auth_channel) if auth_channel and id_pattern.search(auth_channel) else None
AUTH_GROUPS = [int(ch) for ch in auth_grp.split()] if auth_grp else None

DATABASE_URI = environ.get('DATABASE_URI', "mongodb+srv://saidalimuhamed88:iladias2025@cluster0.qt4dv.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
DATABASE_NAME = environ.get('DATABASE_NAME', "Cluster0")
COLLECTION_NAME = environ.get('COLLECTION_NAME', 'Telegram_files')

LOG_CHANNEL = int(environ.get('LOG_CHANNEL', '-100233236188'))
SUPPORT_CHAT = environ.get('SUPPORT_CHAT', 'None')
P_TTI_SHOW_OFF = is_enabled(environ.get('P_TTI_SHOW_OFF', "False"), False)
IMDB = is_enabled(environ.get('IMDB', "True"), True)
SINGLE_BUTTON = is_enabled(environ.get('SINGLE_BUTTON', "True"), True)
CUSTOM_FILE_CAPTION = environ.get("CUSTOM_FILE_CAPTION", None)
BATCH_FILE_CAPTION = environ.get("BATCH_FILE_CAPTION", CUSTOM_FILE_CAPTION)
IMDB_TEMPLATE = environ.get("IMDB_TEMPLATE", "<b>Query: {query}</b> \n‌‌‌‌IMDb Data:\n\n🏷 Title: <a href={url}>{title}</a>\n🎭 Genres: {genres}\n📆 Year: <a href={url}/releaseinfo>{year}</a>\n🌟 Rating: <a href={url}/ratings>{rating}</a> / 10")
LONG_IMDB_DESCRIPTION = is_enabled(environ.get("LONG_IMDB_DESCRIPTION", "False"), False)
SPELL_CHECK_REPLY = is_enabled(environ.get("SPELL_CHECK_REPLY", "True"), True)
MAX_LIST_ELM = environ.get("MAX_LIST_ELM", None)
INDEX_REQ_CHANNEL = int(environ.get('INDEX_REQ_CHANNEL', LOG_CHANNEL))
FILE_STORE_CHANNEL = [int(ch) for ch in (environ.get('FILE_STORE_CHANNEL', '')).split()]
MELCOW_NEW_USERS = is_enabled(environ.get('MELCOW_NEW_USERS', "True"), True)
PROTECT_CONTENT = is_enabled(environ.get('PROTECT_CONTENT', "False"), False)
PUBLIC_FILE_STORE = is_enabled(environ.get('PUBLIC_FILE_STORE', "True"), True)

LOG_STR = "Current Customized Configurations are:-\n"
LOG_STR += ("IMDB Results are enabled, Bot will be showing imdb details for your queries.\n" if IMDB else "IMDB Results are disabled.\n")
LOG_STR += ("P_TTI_SHOW_OFF found, Users will be redirected to send /start to Bot PM instead of sending file directly\n" if P_TTI_SHOW_OFF else "P_TTI_SHOW_OFF is disabled, files will be sent in PM.\n")
LOG_STR += ("SINGLE_BUTTON is enabled: filename and file size shown in a single button\n" if SINGLE_BUTTON else "SINGLE_BUTTON is disabled: filename and size shown separately\n")
LOG_STR += (f"CUSTOM_FILE_CAPTION enabled: {CUSTOM_FILE_CAPTION}\n" if CUSTOM_FILE_CAPTION else "No CUSTOM_FILE_CAPTION Found, default will be used.\n")
LOG_STR += ("Long IMDB storyline enabled.\n" if LONG_IMDB_DESCRIPTION else "Long IMDB storyline disabled.\n")
LOG_STR += ("Spell Check Mode is enabled.\n" if SPELL_CHECK_REPLY else "Spell Check Mode is disabled.\n")
LOG_STR += (f"MAX_LIST_ELM is set to {MAX_LIST_ELM}\n" if MAX_LIST_ELM else "Full list will be shown unless MAX_LIST_ELM is set.\n")
LOG_STR += f"Your current IMDB template is: \n{IMDB_TEMPLATE}"

UPSTREAM_REPO = environ.get('UPSTREAM_REPO', 'https://github.com/oomb')

AUTO_DELETE_SECONDS = int(environ.get('AUTO_DELETE_SECONDS', 300))
AUTO_DELETE = environ.get('AUTO_DELETE', True)
if AUTO_DELETE == "True":
    AUTO_DELETE = True

SHORTNER_SITE = ""
SHORTNER_API = ""

# ---- Flask server for Koyeb health check ----
app = Flask(__name__)

@app.route('/')
def home():
    return "Bot is running!"

def run_web():
    app.run(host="0.0.0.0", port=8000)

# Start Flask server in background
threading.Thread(target=run_web).start()

# ---- You should now start your Telegram bot here ----
# Example if using Pyrogram:
# from pyrogram import Client
# bot = Client(SESSION, api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)
# print(LOG_STR)
# bot.run()