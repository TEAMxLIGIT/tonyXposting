# joinleave.py

import re
from pyrogram import Client, filters, InlineKeyboardButton, InlineKeyboardMarkup
from pyrogram.types import Message
from config import userbot_string_sessions, owner_id

# Create clients for each userbot session
userbot_clients = {session: Client(session) for session in userbot_string_sessions}

async def start_userbots():
    # Start each userbot
    for userbot_client in userbot_clients.values():
        await userbot_client.start()

async def stop_userbots():
    # Stop each userbot
    for userbot_client in userbot_clients.values():
        await userbot_client.stop()

@app.on_message(filters.regex(r'[.,/]') & filters.user(owner_id))
async def handle_joinleave_command(_, message: Message):
    await process_joinleave_command(message)

async def process_joinleave_command(message: Message):
    command_pattern = re.compile(r'[.,/](?:join|leave)\s(@\S+|https://t\.me/\S+)')
    match = command_pattern.match(message.text)

    if match:
        target = match.group(1)

        # Send join/leave command to each userbot
        for userbot_client in userbot_clients.values():
            await userbot_client.send_message(target, "/start")

        reply_text = f"Processed command for all userbots: {message.text}"
    else:
        reply_text = "Invalid join/leave command format. Use '/join @group' or '/leave @group'."

    await message.reply_text(reply_text)

if __name__ == "__main__":
    app = Client(userbot_string_sessions[0])  # Assuming the first string session is used for the main userbot
    app.loop.run_until_complete(start_userbots())
    app.run()
    app.loop.run_until_complete(stop_userbots())