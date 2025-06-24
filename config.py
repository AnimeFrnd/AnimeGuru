import os
import logging
from logging.handlers import RotatingFileHandler


def get_int_env(var_name, default):
    try:
        return int(os.environ.get(var_name, default))
    except ValueError:
        return default  # Fallback to default if conversion fails


def str_to_bool(value):
    return str(value).lower() in ("true", "1", "yes")


BOT_TOKEN = os.environ.get("BOT_TOKEN", "7554699590:AAFaTkdKt7nDrGt-gUW_OTI2DzZVHWj7Lk8")
API_ID = get_int_env("API_ID", 7515868)
API_HASH = os.environ.get("API_HASH", "dbd251e9ad4883b0443cc82b618ac6fa")

OWNER_ID = get_int_env("OWNER_ID", 6081617163)
DB_URL = os.environ.get("DB_URL", "mongodb+srv://bestanimeandcartoonsclips:VrMTuRFUEZdKsoV7@cluster0.ayqz3o3.mongodb.net/?retryWrites=true&w=majority")
DB_NAME = os.environ.get("DB_NAME", "aryabro")

CHANNEL_ID = get_int_env("CHANNEL_ID", -1002292066966)
FORCE_SUB_CHANNEL = get_int_env("FORCE_SUB_CHANNEL", -1001713521586)
FORCE_SUB_CHANNEL2 = get_int_env("FORCE_SUB_CHANNEL2", -1001905224849)
FORCE_SUB_CHANNEL3 = get_int_env("FORCE_SUB_CHANNEL3", -1001864478730)  # Added back
FORCE_SUB_CHANNEL4 = get_int_env("FORCE_SUB_CHANNEL4", -1001712703554)  # Added back

FILE_AUTO_DELETE = get_int_env("FILE_AUTO_DELETE", 86400)  # Auto delete in seconds
PORT = os.environ.get("PORT", "8080")
TG_BOT_WORKERS = get_int_env("TG_BOT_WORKERS", 6)

START_PIC = os.environ.get("START_PIC", "https://telegra.ph/file/703f6dd8194cb5d707d63-c4bfc450283f9a4b4b.jpg")
FORCE_PIC = os.environ.get("FORCE_PIC", "https://telegra.ph/file/703f6dd8194cb5d707d63-c4bfc450283f9a4b4b.jpg")

# Proper handling of admins
ADMINS = {6081617163}  # Use a set to avoid duplicates
env_admins = os.environ.get("ADMINS", "6081617163").split()
ADMINS.update(int(x) for x in env_admins if x.isdigit())  # Ensuring only valid numbers
ADMINS.add(OWNER_ID)  # Ensuring OWNER_ID is in ADMINS
ADMINS = list(ADMINS)  # Convert back to list for compatibility

CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", None)

PROTECT_CONTENT = str_to_bool(os.environ.get('PROTECT_CONTENT', "False"))
DISABLE_CHANNEL_BUTTON = str_to_bool(os.environ.get('DISABLE_CHANNEL_BUTTON', "True"))

BOT_STATS_TEXT = "<b>BOT UPTIME :</b>\n{uptime}"

USER_REPLY_TEXT = "❌sᴏʀʀʏ మావా నువ్వు నా ᴏᴡɴᴇʀ కాదు..!😜\n\n❌Don't Send Me Messages Directly I'm Only File Share Bot !"

START_MSG = """<blockquote>
<b>Hᴇʏ Bʀᴏ, I'ᴍ ᴀ Pᴠᴛ Fɪʟᴇ Sᴛᴏʀᴇ Bᴏᴛ</b>

❓ <b>Hᴏᴡ Tᴏ Usᴇ Mᴇ 🤔❗</b>

- Cʟɪᴄᴋ <b>Start</b> Bᴜᴛᴛᴏɴ  
- Jᴏɪɴ Aʟʟ Rᴇǫᴜɪʀᴇᴅ Cʜᴀɴɴᴇʟs  
- Tʀʏ Aɢᴀɪɴ Aғᴛᴇʀ Jᴏɪɴɪɴɢ

<b>❤‍🩹 - <a href='https://t.me/Arya_Bro_Bot'>@Arya_Bro_Bot</a></b>

<i>(Dᴍ ᴍᴇ ɪғ ʏᴏᴜ'ʀᴇ ғᴀᴄɪɴɢ ᴀɴʏ ɪssᴜᴇs. Rᴇᴘʟɪᴇs ᴍᴀʏ ᴛᴀᴋᴇ sᴏᴍᴇ ᴛɪᴍᴇ.)</i>
</blockquote>"""

FORCE_MSG = "Join my channels first 😈"

LOG_FILE_NAME = "filesharingbot.txt"

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(LOG_FILE_NAME, maxBytes=50000000, backupCount=10),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
