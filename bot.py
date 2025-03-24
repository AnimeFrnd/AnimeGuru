from aiohttp import web
from plugins import web_server #from plugins import admin  # Ensure the new handlers are loaded
import pyromod.listen
from pyrogram import Client, filters
from pyrogram.types import Message
from pyrogram.enums import ParseMode
import sys
from datetime import datetime
from config import API_HASH, API_ID, BOT_TOKEN, TG_BOT_WORKERS, FORCE_SUB_CHANNEL, FORCE_SUB_CHANNEL2, FORCE_SUB_CHANNEL3, FORCE_SUB_CHANNEL4, CHANNEL_ID, PORT, START_MSG
import logging

# Set up the logger
logging.basicConfig(level=logging.INFO)
LOGGER = logging.getLogger(__name__)

import pyrogram
pyrogram.utils.MIN_CHANNEL_ID = -1009999999999  # Fixes channel ID issues

class Bot(Client):
    def __init__(self):
        super().__init__(
            name="Bot",
            api_hash=API_HASH,
            api_id=API_ID,
            plugins={"root": "plugins"},
            workers=TG_BOT_WORKERS,
            bot_token=BOT_TOKEN
        )
        self.LOGGER = LOGGER  # Assign logger instance

    async def start(self):
        await super().start()
        usr_bot_me = await self.get_me()
        self.uptime = datetime.now()

        # Set up invite links for Force Sub Channels
        for sub_channel, invitelink_attr in [
            (FORCE_SUB_CHANNEL, 'invitelink'), 
            (FORCE_SUB_CHANNEL2, 'invitelink2'),
            (FORCE_SUB_CHANNEL3, 'invitelink3'),
            (FORCE_SUB_CHANNEL4, 'invitelink4')
        ]:
            if sub_channel:
                try:
                    link = (await self.get_chat(sub_channel)).invite_link
                    if not link:
                        await self.export_chat_invite_link(sub_channel)
                        link = (await self.get_chat(sub_channel)).invite_link
                    setattr(self, invitelink_attr, link)
                except Exception as e:
                    self.LOGGER.warning(f"Error: {e}")
                    self.LOGGER.warning("Bot can't export invite link from Force Sub Channel!")
                    self.LOGGER.warning(f"Check {sub_channel} and ensure the bot has admin rights with 'Invite Users' permission!")
                    self.LOGGER.info("Bot Stopped. Join https://t.me/Telugu_Movies_999 for Support")
                    sys.exit()

        try:
            db_channel = await self.get_chat(CHANNEL_ID)
            self.db_channel = db_channel
            test = await self.send_message(chat_id=db_channel.id, text="Hey 🖐")
            await test.delete()
        except Exception as e:
            self.LOGGER.warning(f"Error: {e}")
            self.LOGGER.warning("Ensure the bot is admin in the DB Channel and check the CHANNEL_ID value!")
            self.LOGGER.info("Bot Stopped. Join https://t.me/Telugu_Movies_999 for Support")
            sys.exit()

        self.parse_mode = ParseMode.HTML
        self.LOGGER.info("Bot Running..!\n\nCreated By https://t.me/Telugu_Movies_999")
        self.LOGGER.info("ミ💖 Telugu Movies 999 💖彡")
        self.username = usr_bot_me.username

        # Web server setup
        app = web.AppRunner(await web_server())
        await app.setup()
        bind_address = "0.0.0.0"
        await web.TCPSite(app, bind_address, PORT).start()

    async def stop(self, *args):
        await super().stop()
        self.LOGGER.info("Bot Stopped...")

# Start Command with Quote Block
@app.on_message(filters.command("start"))
async def start_message(client: Client, message: Message):
    await message.reply_text(
        START_MSG.format(id=message.from_user.id, first=message.from_user.first_name),
        parse_mode="html"
    )

app = Bot()
app.run()
