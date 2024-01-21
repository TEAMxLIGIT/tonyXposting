# help.py

from pyrogram import Client, filters
from pyrogram.types import Message
from config import userbot_string_sessions, bot_token, owner_id

app = Client('userbot_session', api_id=api_id, api_hash=api_hash, bot_token=bot_token)

@app.on_message(filters.regex(r'[.,/]') & filters.user(owner_id))
async def handle_help_command(_, message: Message):
    await send_help_message(message)

async def send_help_message(message: Message):
    help_text = (
        "**Available Commands:**\n\n"
        "`.post [message]` - Post a message to all groups.\n"
        "`.stop` - Stop the userbot.\n"
        "`.limit` - Send a message to @SpamBot and get the first message.\n"
        "`.broadcast [message]` - Broadcast a message to all groups and chats.\n"
        "`.join [group/channel link]` - Join a group or channel.\n"
        "`.leave [group/channel link]` - Leave a group or channel.\n"
        "`.alive` - Check the userbot's status.\n"
        "`.msgall [message]` - Send a message to recent users in the same group.\n"
        "`.help` - Display this help message."
    )

    await message.reply_text(help_text, parse_mode="markdown")

if __name__ == "__main__":
    app.run()