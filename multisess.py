# multisess.py

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
async def handle_multisess_command(_, message: Message):
    await process_multisess_command(message)

async def process_multisess_command(message: Message):
    command_pattern = re.compile(r'[.,/](?:multisess)\s(start|stop)')
    match = command_pattern.match(message.text)

    if match:
        action = match.group(1)

        if action == 'start':
            await start_userbots()
            reply_text = "Started all userbots."
        elif action == 'stop':
            await stop_userbots()
            reply_text = "Stopped all userbots."
    else:
        reply_text = "Invalid multisess command format. Use '/multisess start' or '/multisess stop'."

    await message.reply_text(reply_text)

if __name__ == "__main__":
    app.loop.run_until_complete(start_userbots())
    app.run()
    app.loop.run_until_complete(stop_userbots())