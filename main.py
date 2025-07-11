import asyncio
from telethon import TelegramClient, events
import os

# Your API credentials
api_id = 21486544
api_hash = 'fabd7b31ac08f72e36ef51c0d8c84861'

# Your Telegram ID (only you can use the bot)
OWNER_ID = 5281036551

client = TelegramClient("anon", api_id, api_hash)

@client.on(events.NewMessage(pattern='/start'))
async def start(event):
    if event.sender_id != OWNER_ID:
        return
    await event.reply("👋 Welcome! Send me a video link (TikTok, X, Instagram, PH) to download.")

@client.on(events.NewMessage())
async def handle(event):
    if event.sender_id != OWNER_ID:
        return

    url = event.raw_text.strip()
    if not url.startswith("http"):
        await event.reply("❌ Please send a valid video link.")
        return

    await event.reply("⏳ Downloading...")

    try:
        filename = "video.mp4"
        os.system(f'yt-dlp -o {filename} "{url}"')

        if os.path.exists(filename):
            await client.send_file(event.chat_id, filename, caption="✅ Done.")
            os.remove(filename)
        else:
            await event.reply("❌ File download failed.")
    except Ex
