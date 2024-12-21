import os
import random
import logging
from os import getenv
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.errors import ChatAdminRequired, RPCError
from typing import Union
import asyncio
from config import LOG_GROUP_ID as LOGGER_ID

LOG_GROUP_ID = int(getenv("LOG_GROUP_ID", "-1002018556839"))

photo = [
    "https://telegra.ph/file/1949480f01355b4e87d26.jpg",
    "https://telegra.ph/file/3ef2cc0ad2bc548bafb30.jpg",
    "https://telegra.ph/file/a7d663cd2de689b811729.jpg",
    "https://telegra.ph/file/6f19dc23847f5b005e922.jpg",
    "https://telegra.ph/file/2973150dd62fd27a3a6ba.jpg",
]

## all clients

app = Client(
    name="App",
    api_id=API_ID,
    api_hash=API_HASH,
    session_string=str(STRING_SESSION),
)

bot = Client(
    name="Bot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN,
)

# Handler for new chat members
@bot.on_message(filters.new_chat_members, group=2)
async def join_watcher(client: Client, message: Message):
    try:
        chat = message.chat
        link = await client.export_chat_invite_link(chat.id)
        for member in message.new_chat_members:
            if member.id == (await client.get_me()).id:
                count = await client.get_chat_members_count(chat.id)
                msg = (
                    f"📝 ᴍᴜsɪᴄ ʙᴏᴛ ᴀᴅᴅᴇᴅ ɪɴ ᴀ ɴᴇᴡ ɢʀᴏᴜᴘ\n\n"
                    f"____________________________________\n\n"
                    f"📌 ᴄʜᴀᴛ ɴᴀᴍᴇ: {chat.title}\n"
                    f"🍂 ᴄʜᴀᴛ ɪᴅ: {chat.id}\n"
                    f"🔐 ᴄʜᴀᴛ ᴜsᴇʀɴᴀᴍᴇ: @{chat.username or 'N/A'}\n"
                    f"🛰 ᴄʜᴀᴛ ʟɪɴᴋ: [ᴄʟɪᴄᴋ]({link})\n"
                    f"📈 ɢʀᴏᴜᴘ ᴍᴇᴍʙᴇʀs: {count}\n"
                    f"🤔 ᴀᴅᴅᴇᴅ ʙʏ: {message.from_user.mention}"
                )
                await client.send_photo(
                    LOGGER_ID,
                    photo=random.choice(photo),
                    caption=msg,
                    reply_markup=InlineKeyboardMarkup([
                        [InlineKeyboardButton("sᴇᴇ ɢʀᴏᴜᴘ👀", url=link)]
                    ])
                )
    except RPCError as e:
        logging.error(f"Error in join_watcher: {e}")

# Handler for when the bot leaves a chat
@bot.on_message(filters.left_chat_member)
async def on_left_chat_member(client: Client, message: Message):
    try:
        if (await client.get_me()).id == message.left_chat_member.id:
            remove_by = message.from_user.mention if message.from_user else "ᴜɴᴋɴᴏᴡɴ ᴜsᴇʀ"
            title = message.chat.title
            username = f"@{message.chat.username}" if message.chat.username else "ᴘʀɪᴠᴀᴛᴇ ᴄʜᴀᴛ"
            chat_id = message.chat.id
            bot_username = (await client.get_me()).username
            left_msg = (
                f"📞 <b><u>ᴍᴜsɪᴄ ʙᴏᴛ ʀᴇᴍᴏᴠᴇᴅ ᴀ ɢʀᴏᴜᴘ</u></b> 🗑️\n\n"
                f"📌 ᴄʜᴀᴛ ᴛɪᴛʟᴇ: {title}\n\n"
                f"🗒️ ᴄʜᴀᴛ ɪᴅ: {chat_id}\n\n"
                f"🔨 ʀᴇᴍᴏᴠᴇᴅ ʙʏ: {remove_by}\n\n"
                f"🗑️ ʙᴏᴛ: @{bot_username}"
            )
            await client.send_photo(
                LOGGER_ID,
                photo=random.choice(photo),
                caption=left_msg
            )
    except RPCError as e:
        logging.error(f"Error in on_left_chat_member: {e}")

