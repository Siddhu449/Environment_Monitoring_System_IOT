import logging
import yt_dlp
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

# Enable logging to track errors and updates
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

# Enable debug-level logging for httpx
logging.getLogger("httpx").setLevel(logging.DEBUG)

logger = logging.getLogger(__name__)

# Define a command to start the bot
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Hello! Send me a URL from YouTube, and I will try to find the music for you!"
    )

# Function to fetch music from YouTube link
def fetch_music_from_url(url):
    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': 'downloads/%(id)s.%(ext)s',
        'quiet': True,
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info_dict = ydl.extract_info(url, download=False)
        audio_url = info_dict.get('url', None)
        title = info_dict.get('title', None)
        return title, audio_url

# Function to handle messages and fetch music info from provided URLs
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    url = update.message.text
    if "youtube" in url:
        try:
            title, audio_url = fetch_music_from_url(url)
            if title and audio_url:
                await update.message.reply_text(f"Song Name: {title}")
                await update.message.reply_text(f"Download link: {audio_url}")
        except Exception as e:
            await update.message.reply_text(f"Error fetching music: {str(e)}")
    else:
        await update.message.reply_text(
            "Sorry, I can only fetch music from YouTube at the moment."
        )

# Main function to start the bot
def main():
    # Replace 'YOUR_TOKEN' with your bot's token
    TOKEN = "7492642687:AAFmhu5QkubmUf5OsuQmhmbLxiP6qiILqXk"
    application = Application.builder().token(TOKEN).build()

    # Add command and message handlers
    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    # Start the Bot
    application.run_polling()

if __name__ == '__main__':
    main()
