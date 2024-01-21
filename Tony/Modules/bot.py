# bot.py

from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from config import bot_token, bot_session_name, owner_id

app = Client(bot_session_name, bot_token=bot_token)

# Dictionary to store connected userbots
connected_userbots = {}

@app.on_message(filters.command("start") | filters.private)
async def start_command_handler(_, message):
    user = message.from_user
    first_name = user.first_name

    # Create an InlineKeyboardMarkup with support group and channel buttons
    keyboard = InlineKeyboardMarkup(
        [[
            InlineKeyboardButton("Support Group", url="https://t.me/sastatony"),
            InlineKeyboardButton("Support Channel", url="https://t.me/team_ligit")
        ]]
    )

    # Updated greet message with .mp4 link and /clone command
    greet_message = (
        f"Hello {first_name},\n\n"
        "This Auto Posting Userbot is created by @poolnft.\n"
        "Use /clone {pyrogramV2 session} to add more userbots.\n"
        "[Watch the Introduction Video](https://te.legra.ph/file/e47973f5c54a125ec49aa.mp4)"
    )

    await message.reply_text(
        greet_message,
        reply_markup=keyboard,
        disable_web_page_preview=True,
        parse_mode="markdown"
    )

@app.on_message(filters.command("clone") & filters.user(owner_id))
async def clone_command_handler(_, message):
    try:
        # Extract the Pyrogram V2 string session from the command
        _, session = message.text.split(" ", 1)

        # Connect the new userbot
        new_userbot = Client(session)
        connected_userbots[session] = new_userbot

        await new_userbot.start()

        await message.reply_text("Userbot cloned successfully and started.")
    except Exception as e:
        await message.reply_text(f"Error while cloning userbot: {str(e)}")

if __name__ == "__main__":
    app.run()