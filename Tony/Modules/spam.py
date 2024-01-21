# spam.py

import asyncio
from pyrogram import Client, filters
from pyrogram.types import Message
from config import api_id, api_hash, bot_token, owner_id, session_name

app = Client(session_name, api_id=api_id, api_hash=api_hash, bot_token=bot_token)

# Variable to keep track of whether the userbot should continue running
userbot_running = True

@app.on_message(filters.regex(r'[.,/]') & filters.user(owner_id))
async def handle_limit_command(_, message: Message):
    global userbot_running

    if userbot_running and message.text.startswith(',"/limit'):
        await send_to_spam_bot(message)

async def send_to_spam_bot(message: Message):
    await message.reply_chat_action("typing")
    await asyncio.sleep(2)  # Adjust the time delay if needed

    # Send '/start' command to @SpamBot
    sent_message = await app.send_message('SpamBot', '/start')

    # Reply with the first message from @SpamBot to the chat or group
    reply_text = f"Userbot response from @SpamBot:\n\n{sent_message.text}"
    await message.reply_text(reply_text)

if __name__ == "__main__":
    app.run()