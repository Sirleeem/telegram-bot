import os
from telethon import TelegramClient

api_id = int(os.environ.get("API_ID"))
api_hash = os.environ.get("API_HASH")
session_name = os.environ.get("SESSION", "anon")

client = TelegramClient(session_name, api_id, api_hash)

async def main():
    print("Bot is running...")

with client:
    client.loop.run_until_complete(main())
