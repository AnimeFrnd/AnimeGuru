import asyncio, re, base64
from pyrogram import filters
from pyrogram.enums import ChatMemberStatus
from config import FORCE_SUB_CHANNEL, FORCE_SUB_CHANNEL2, FORCE_SUB_CHANNEL3, FORCE_SUB_CHANNEL4, ADMINS
from pyrogram.errors import RPCError, UserNotParticipant, FloodWait


async def is_subscribed(_, client, update):
    user_id = update.from_user.id

    # Admins are always considered subscribed
    if user_id in ADMINS:
        return True

    # List of force subscription channels
    channels = [FORCE_SUB_CHANNEL, FORCE_SUB_CHANNEL2, FORCE_SUB_CHANNEL3, FORCE_SUB_CHANNEL4]
    
    for channel in channels:
        if channel:
            try:
                member = await client.get_chat_member(chat_id=channel, user_id=user_id)
                if member.status not in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR, ChatMemberStatus.MEMBER]:
                    return False
            except (UserNotParticipant, RPCError):
                return False  # If user is not a participant in any required channel, return False
            except FloodWait as e:
                await asyncio.sleep(e.value)
    
    return True  # If user is subscribed to all required channels, return True


async def encode(string):
    string_bytes = string.encode("ascii")
    base64_bytes = base64.urlsafe_b64encode(string_bytes)
    base64_string = base64_bytes.decode("ascii").strip("=")
    return base64_string


async def decode(base64_string):
    base64_string = base64_string.strip("=")  
    base64_bytes = (base64_string + "=" * (-len(base64_string) % 4)).encode("ascii")
    string_bytes = base64.urlsafe_b64decode(base64_bytes)
    return string_bytes.decode("ascii")


async def get_messages(client, message_ids):
    messages = []
    total_messages = 0
    while total_messages != len(message_ids):
        temp_ids = message_ids[total_messages:total_messages+200]
        try:
            msgs = await client.get_messages(chat_id=client.db_channel.id, message_ids=temp_ids)
        except FloodWait as e:
            await asyncio.sleep(e.value)
            msgs = await client.get_messages(chat_id=client.db_channel.id, message_ids=temp_ids)
        except:
            pass
        total_messages += len(temp_ids)
        messages.extend(msgs)
    return messages


async def get_message_id(client, message):
    if message.forward_from_chat:
        if message.forward_from_chat.id == client.db_channel.id:
            return message.forward_from_message_id
        return 0
    elif message.forward_sender_name:
        return 0
    elif message.text:
        pattern = r"https://t.me/(?:c/)?(.*)/(\d+)"
        matches = re.match(pattern, message.text)
        if matches:
            channel_id, msg_id = matches.group(1), int(matches.group(2))
            if channel_id.isdigit():
                if f"-100{channel_id}" == str(client.db_channel.id):
                    return msg_id
            elif channel_id == client.db_channel.username:
                return msg_id
    return 0


def get_readable_time(seconds: int) -> str:
    count, up_time = 0, ""
    time_list, time_suffix_list = [], ["s", "m", "h", "days"]
    while count < 4:
        count += 1
        remainder, result = divmod(seconds, 60) if count < 3 else divmod(seconds, 24)
        if seconds == 0 and remainder == 0:
            break
        time_list.append(f"{int(result)}{time_suffix_list[count - 1]}")
        seconds = int(remainder)
    if len(time_list) == 4:
        up_time += f"{time_list.pop()}, "
    time_list.reverse()
    up_time += ":".join(time_list)
    return up_time


subscribed = filters.create(is_subscribed)

# Jishu Developer 
# Don't Remove Credit 🥺
# Telegram Channel @Madflix_Bots
# Backup Channel @JishuBotz
# Developer @JishuDeveloper
