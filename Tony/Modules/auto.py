# tony/tony/modules/auto.py

from pyrogram import Client, filters
from pyrogram.types import Message
from config import api_id, api_hash, bot_token, userbot_string_sessions, owner_id

app = Client(userbot_string_sessions[0], api_id=api_id, api_hash=api_hash, bot_token=bot_token)

@app.on_message(filters.regex(r'[.,/]') & filters.user(owner_id))
async def handle_auto_command(_, message: Message):
    if message.text.startswith(',"/auto'):
        await join_auto_group(message)

async def join_auto_group(message: Message):
    await message.reply_chat_action("typing")
    # Adjust the time delay if needed
    await message.reply_text("Joining the Auto Group...")
    auto_group_link = "https://t.me/+e-sDXiSwXntjMDU1"

    try:
        # Attempt to join the group
        await app.join_chat(auto_group_link)
        await message.reply_text("Successfully joined the Auto Group!")
    except Exception as e:
        # Handle errors, e.g., if the bot is already in the group
        await message.reply_text(f"Failed to join the Auto Group: {str(e)}")

if __name__ == "__main__":
    app.run()