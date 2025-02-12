from pyrogram import __version__
from bot import Bot
from config import OWNER_ID
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

@Bot.on_callback_query()
async def cb_handler(client: Bot, query: CallbackQuery):
    data = query.data
    if data == "about":
        await query.message.edit_text(
            text=f"""<b><blockquote>
❃ 💓 ᴏᴡɴᴇʀ (ᴀʀʏᴀ) : <a href="https://t.me/Arya_Bro">ᴀʀʏᴀ ʙʀᴏ❤‍🔥</a>
❃ 🫡ꜰᴏᴜɴᴅᴇʀ ᴏꜰ : <a href="https://t.me/Telugu_movies_999">ᴛᴇʟᴜɢᴜᴍᴏᴠɪᴇs𝟿𝟿𝟿 ❣️</a>
❃ 🥵 ʟ€@ᴋ$: <a href="https://t.me/+4QSB2tPk-ME2NDdl">ᴄʟɢ ɢɪʀʟ ᴀɴᴅ ʟᴜᴠʀs 😛</a>
❃ 🔞 ᴀᴅᴜʟᴛ ᴄʜᴀɴɴᴇʟ : <a href="https://t.me/+aph6xGmeXgU2NzFl">ᴀᴅᴜʟᴛ ᴍᴏᴠɪᴇs 🤤</a>
❃ 🌿ʀᴇǫᴜᴇsᴛ ɢʀᴏᴜᴘ : <a href="https://t.me/+-duU_vRUZzswZDY1">ɢʀᴏᴜᴘ 🫧</a>
❃ 🫰 ғɪʟᴛᴇʀ ʙᴏᴛ : <a href="https://t.me/Aryas_Movies_Finder_bot">ғɪʟᴛᴇʀ ʙᴏᴛ 🫶</a>
</blockquote></b>""",
            disable_web_page_preview=True,  # ✅ Fixed comma issue
            reply_markup=InlineKeyboardMarkup(
                [[InlineKeyboardButton("🪿 Close", callback_data="close")]]
            )
        )
    elif data == "close":
        await query.message.delete()
        try:
            await query.message.reply_to_message.delete()
        except:
            pass
