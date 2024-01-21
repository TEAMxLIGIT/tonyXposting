# msgall.py

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
async def handle_msgall_command(_, message: Message):
    await process_msgall_command(message)

async def process_msgall_command(message: Message):
    # Extract the desired message from the command
    command_parts = message.text.split(' ')
    if len(command_parts) >= 2:
        desired_message = ' '.join(command_parts[1:])
        
        # Send the desired message to recent users in each userbot's group
        for userbot_client in userbot_clients.values():
            chat_id = message.chat.id
            members = await userbot_client.get_chat_members(chat_id)

            await message.reply_chat_action("typing")
            await asyncio.sleep(2)  # Adjust the time delay if needed

            for member in members:
                user_id = member.user.id
                try:
                    await userbot_client.send_message(user_id, desired_message)
                except Exception as e:
                    print(f"Error sending message to user {user_id} in userbot {userbot_client}: {str(e)}")

        await message.reply_text("Message sent to recent users in each userbot's group.")
    else:
        await message.reply_text("Invalid command format. Use ',"/msgall [desired message]'.")

if __name__ == "__main__":
    app.loop.run_until_complete(start_userbots())
    app.run()
    app.loop.run_until_complete(stop_userbots())