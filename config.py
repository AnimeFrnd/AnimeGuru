import os
import logging
from logging.handlers import RotatingFileHandler




BOT_TOKEN = os.environ.get("BOT_TOKEN", "6401414916:AAHx2_MGbexWEMecwIXXBzz42t2dHXKmTX4")
API_ID = int(os.environ.get("API_ID", "7515868"))
API_HASH = os.environ.get("API_HASH", "dbd251e9ad4883b0443cc82b618ac6fa")


OWNER_ID = int(os.environ.get("OWNER_ID", "6081617163"))
DB_URL = os.environ.get("DB_URL", "mongodb+srv://bestanimeandcartoonsclips:VrMTuRFUEZdKsoV7@cluster0.ayqz3o3.mongodb.net/?retryWrites=true&w=majority")
DB_NAME = os.environ.get("DB_NAME", "aryabro")


CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1002292066966"))
FORCE_SUB_CHANNEL = int(os.environ.get("FORCE_SUB_CHANNEL", "-1001507915878"))
FORCE_SUB_CHANNEL2 = int(os.environ.get("FORCE_SUB_CHANNEL2", "-1001798300759"))
FORCE_SUB_CHANNEL3 = int(os.environ.get("FORCE_SUB_CHANNEL3", "-1001981549906"))
FORCE_SUB_CHANNEL4 = int(os.environ.get("FORCE_SUB_CHANNEL4", "-1002009379876"))


FILE_AUTO_DELETE = int(os.getenv("FILE_AUTO_DELETE", "86400")) # auto delete in seconds


PORT = os.environ.get("PORT", "8080")
TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "6"))



try:
    ADMINS=[6081617163]
    for x in (os.environ.get("ADMINS", "6081617163").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")









CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", None)

PROTECT_CONTENT = True if os.environ.get('PROTECT_CONTENT', "False") == "True" else False

DISABLE_CHANNEL_BUTTON = True if os.environ.get('DISABLE_CHANNEL_BUTTON', "True") == "True" else False

BOT_STATS_TEXT = "<b>BOT UPTIME :</b>\n{uptime}"







USER_REPLY_TEXT = "❌sᴏʀʀʏ మావా నువ్వు నా ᴏᴡɴᴇʀ కాదు..!😜\n\n❌Don't Send Me Messages Directly I'm Only File Share Bot !"

START_MSG = os.environ.get("START_MESSAGE", "Orey!!{mention}\n\nI Can Store Private Files In Specified Channel And Other Users Can Access It From Special Link.\n\n Developed By - @Telugu_Movies_999 ❣️")

FORCE_MSG = os.environ.get("FORCE_SUB_MESSAGE", "Hello {mention}\n\n<b>ʏᴏᴜ ɴᴇᴇᴅ ᴛᴏ ᴊᴏɪɴ ᴏᴜʀ ᴄʜᴀɴɴᴇʟs ᴀɴᴅ ᴛʜᴇɴ ᴄʟɪᴄᴋ ᴏɴ ʀᴇʟᴏᴀᴅ button ᴛᴏ ɢᴇᴛ ʏᴏᴜʀ ʀᴇǫᴜᴇꜱᴛᴇᴅ ꜰɪʟᴇ. \n\n కింద ఇచ్చిన 4 చానెల్స్ లో జాయిన్ అయ్యి తరవాత Try Again క్లిక్ చేస్తే File📁 వస్తది..:) 🥰</b>")





ADMINS.append(OWNER_ID)
ADMINS.append(6081617163)

LOG_FILE_NAME = "filesharingbot.txt"

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            LOG_FILE_NAME,
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
   





# Jishu Developer 
# Don't Remove Credit 🥺
# Telegram Channel @Madflix_Bots
# Backup Channel @JishuBotz
# Developer @JishuDeveloper
