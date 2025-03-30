from pyrogram import __version__
from bot import Bot
from config import OWNER_ID
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

@Bot.on_callback_query()
async def cb_handler(client: Bot, query: CallbackQuery):
    data = query.data
    if data == "about":
        await query.message.edit_text(
            text =  f'<b>⟦★⟧ Hi There {query.from_user.mention}</b>!💫\n' \
                  f'<b>┏━━━━━━━❪❂❫━━━━━━━━</b>\n' \
                  f'◈ <b>Cʀᴇᴀᴛᴏʀ</b>: <b><a href="https://t.me/Nithya_Sree_Bot">𝓝𝓲𝓽𝓱𝔂𝓪 𝓼𝓱𝓻𝓮𝓮 🥀🦋</a></b>\n' \
                  f'◈ <b>Fᴏᴜɴᴅᴇʀ ᴏꜰ</b>: <b><a href="https://t.me/+_Y54DFBnaVUwZjc1">Dᴏᴏᴛʜᴀ</a></b>\n' \
                  f'◈ <b>Oɴɢᴏɪɴɢ Cʜᴀɴɴᴇʟ</b>: <b><a href="https://t.me/anime_Movies_and_Series_Telugu">Oɴɢᴏɪɴɢ Aɴɪᴍᴇ</a></b>\n' \
                  f'◈ <b>Mᴀɪɴ Cʜᴀɴɴᴇʟ</b>: <b><a href="https://t.me/Telugu_Movies_999">Mᴀɪɴ Cʜᴀɴɴᴇʟ</a></b>\n' \
                  f'◈ <b>Tᴇʟᴜɢᴜ Mᴏᴠɪᴇs</b>: <b><a href="https://t.me/vs_Files_Mx_player">Oᴜʀ Bᴏᴛs </a></b>\n' \
                  f'◈ <b>Dᴇᴠᴇʟᴏᴘᴇʀ</b>: <b><a href="https://t.me/arya_Bro_Bot">𝐀ʀʏᴀ</a></b>\n' \
                  f'<b>┗━━━━━━━❪❂❫━━━━━━━━</b>', 
            disable_web_page_preview=True,  # ✅ Added missing comma
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("🪿 Close", callback_data="close")
                    ]
                ]
            )
        )
    elif data == "close":
        await query.message.delete()
        try:
            await query.message.reply_to_message.delete()
        except:
            pass
