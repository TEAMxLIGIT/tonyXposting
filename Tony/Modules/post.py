# post.py

import asyncio
from pyrogram import Client, filters
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
async def handle_post(_, message: Message):
    await process_post_command(message)

async def process_post_command(message: Message):
    global userbot_running

    if userbot_running:
        if message.text.startswith('.post') or message.text.startswith('/post') or message.text.startswith(',"/post'):
            post_text = message.text[6:]  # Adjust the index based on your command structure
            send_time = 30  # Adjust the time delay as needed (in seconds)

            # Send the post to all userbots
            for userbot_client in userbot_clients.values():
                dialogs = await userbot_client.get_dialogs()
                for dialog in dialogs:
                    if dialog.chat.type in ["group", "supergroup"]:
                        await message.reply_chat_action("typing")
                        await asyncio.sleep(send_time)
                        await userbot_client.send_message(dialog.chat.id, post_text)
        elif message.text.startswith('.stop') or message.text.startswith('/stop') or message.text.startswith(',"/stop'):
            userbot_running = False
            await message.reply_text('Userbot stopped.')

if __name__ == "__main__":
    app.loop.run_until_complete(start_userbots())
    app.run()
    app.loop.run_until_complete(stop_userbots())