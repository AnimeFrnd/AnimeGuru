from pyrogram import Client, filters
from config import ADMINS

@Client.on_message(filters.command("addadmin") & filters.user(ADMINS))
async def add_admin(client, message):
    if len(message.command) < 2:
        return await message.reply("Usage: /addadmin <user_id>")
    
    new_admin = int(message.command[1])
    if new_admin not in ADMINS:
        ADMINS.append(new_admin)
        await message.reply(f"✅ Added {new_admin} as admin!")
    else:
        await message.reply("⚠️ User is already an admin!")

@Client.on_message(filters.command("removeadmin") & filters.user(ADMINS))
async def remove_admin(client, message):
    if len(message.command) < 2:
        return await message.reply("Usage: /removeadmin <user_id>")
    
    remove_admin = int(message.command[1])
    if remove_admin in ADMINS:
        ADMINS.remove(remove_admin)
        await message.reply(f"✅ Removed {remove_admin} from admins!")
    else:
        await message.reply("⚠️ User is not an admin!")

@Client.on_message(filters.command("admins") & filters.user(ADMINS))
async def list_admins(client, message):
    await message.reply(f"👑 **Admin List:**\n" + "\n".join(map(str, ADMINS)))
