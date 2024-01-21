# alive.py

import asyncio
from datetime import datetime
from pyrogram import Client, filters, InlineKeyboardButton, InlineKeyboardMarkup
from pyrogram.types import Message
from config import userbot_string_sessions, owner_id

# Create a dictionary to store userbot start times
userbot_start_times = {session: datetime.now() for session in userbot_string_sessions}

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

app = Client(userbot_string_sessions[0])  # Assuming the first string session is used for the main userbot

# Variable to keep track of userbot start time
main_userbot_start_time = datetime.now()

@app.on_message(filters.regex(r'[.,/]') & filters.user(owner_id))
async def handle_alive_command(_, message: Message):
    await send_alive_message(message)

async def send_alive_message(message: Message):
    global main_userbot_start_time

    # Calculate main userbot uptime
    main_userbot_uptime = datetime.now() - main_userbot_start_time
    main_userbot_uptime_str = str(main_userbot_uptime).split('.')[0]

    # Create an InlineKeyboardMarkup with support group and repo buttons
    keyboard = InlineKeyboardMarkup(
        [[
            InlineKeyboardButton("Support Group", url="https://t.me/sastatony"),
            InlineKeyboardButton("Repo", url="https://t.me/team_ligit")
        ]]
    )

    # Add telegraph .mp4 link below other information
    alive_message = (
        f"**Main Userbot Status**\n\n"
        f"**Owner:** {owner_id}\n"
        f"**Pyrogram Version:** {Client.__version__}\n"
        f"**Uptime:** {main_userbot_uptime_str}\n\n"
        f"[Watch the Alive Video](https://telegra.ph/bhaii_link_dede-01-21)"
    )

    await message.reply_text(
        alive_message,
        reply_markup=keyboard,
        parse_mode="markdown"
    )

if __name__ == "__main__":
    app.loop.run_until_complete(start_userbots())
    app.run()
    app.loop.run_until_complete(stop_userbots())