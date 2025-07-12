import asyncio
from telethon import TelegramClient, events
import os

# Your API credentials
api_id = 
api_hash = ''

# Your Telegram ID
OWNER_ID = 

# Use existing session file
client = TelegramClient("anon", api_id, api_hash)

@client.on(events.NewMessage(pattern='/start'))
async def start(event):
    if event.sender_id != OWNER_ID:
        return
    await event.reply("👋 Welcome! Send me a video link to download (TikTok, X, IG, etc).")

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
            await event.reply("❌ Failed to download file.")
    except Exception as e:
        await event.reply(f"⚠️ Error: {str(e)}")

with client:
    print("✅ Bot is running...")
    client.run_until_disconnected()
