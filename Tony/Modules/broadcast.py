# broadcast.py

import asyncio
from pyrogram import Client
from pyrogram.types import Message
from config import userbot_string_sessions

async def broadcast_message(app: Client, message: Message):
    # Extracting the reply message if it exists
    reply_message = message.reply_to_message

    # Broadcast the reply message or the original message with media to all userbots
    for userbot_string_session in userbot_string_sessions:
        # Use each userbot's string session to initialize a new userbot client
        userbot = Client(userbot_string_session)
        await userbot.start()

        dialogs = await userbot.get_dialogs()
        for dialog in dialogs:
            if dialog.chat.type in ["group", "supergroup"]:
                await message.reply_chat_action("typing")
                await asyncio.sleep(5)  # Adjust the time delay if needed

                if reply_message:
                    await userbot.send_message(dialog.chat.id, reply_message.text)
                elif message.text:
                    await userbot.send_message(dialog.chat.id, message.text)

        # Stop the userbot session after broadcasting to a specific userbot
        await userbot.stop()

if __name__ == "__main__":
    # This is just a script for testing the broadcast
    with Client(userbot_string_sessions[0]) as app:  # Assuming userbot_string_sessions is a list
        message = Message(message_id=123)  # Replace with an actual Message object
        app.loop.run_until_complete(broadcast_message(app, message))