from pyrogram import Client, filters
from config import ADMINS, OWNER_ID

@Client.on_message(filters.command("addadmin") & filters.user(ADMINS))
async def add_admin(client, message):
    if len(message.command) < 2:
        return await message.reply("Usage: /addadmin <user_id>")
    
    try:
        new_admin = int(message.command[1])
        if new_admin not in ADMINS:
            ADMINS.append(new_admin)
            await message.reply(f"✅ Added {new_admin} as admin!")
        else:
            await message.reply("⚠️ User is already an admin!")
    except ValueError:
        await message.reply("❌ Invalid user ID!")

@Client.on_message(filters.command("removeadmin") & filters.user(ADMINS))
async def remove_admin(client, message):
    if len(message.command) < 2:
        return await message.reply("Usage: /removeadmin <user_id>")
    
    try:
        remove_admin = int(message.command[1])
        if remove_admin in ADMINS and remove_admin != OWNER_ID:
            ADMINS.remove(remove_admin)
            await message.reply(f"✅ Removed {remove_admin} from admins!")
        else:
            await message.reply("⚠️ Cannot remove owner or non-admin user!")
    except ValueError:
        await message.reply("❌ Invalid user ID!")

@Client.on_message(filters.command("admins") & filters.user(ADMINS))
async def list_admins(client, message):
    admin_list = "\n".join(map(str, ADMINS))
    await message.reply(f"👑 **Admin List:**\n{admin_list}")
