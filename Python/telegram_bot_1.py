from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes

# Command handler for the /start command
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    # Create a button linking to your GitHub account
    keyboard = [[InlineKeyboardButton("Visit My GitHub", url="https://github.com/kartos125?tab=projects")]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text("Welcome! Click the button below to visit my GitHub account.", reply_markup=reply_markup)

# Callback for when the user interacts with the bot
async def github_callback(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = update.callback_query
    await query.answer()  # Acknowledge the button click

    # After visiting GitHub, provide a link to your YouTube video
    await query.message.reply_text("Thank you for visiting my GitHub! Here's my YouTube video link:\n"
                                    "https://youtu.be/lX36WupIkQg?si=SDZEjfh0soYIXMg1")

# Command handler for the /help command
async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("You can control me by sending these commands:\n"
                                    "/start - Start interacting with the bot\n"
                                    "/help - Get this help message")

# Main function to start the bot
def main():
    # Replace 'YOUR_BOT_TOKEN' with your bot token from BotFather
    bot_token = '7492642687:AAFmhu5QkubmUf5OsuQmhmbLxiP6qiILqXk'

    # Create the Application instance
    application = Application.builder().token(bot_token).build()

    # Register command handlers
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))

    # Register a callback query handler for button interactions
    application.add_handler(CallbackQueryHandler(github_callback))

    # Start the bot
    application.run_polling()
    print("Bot is running...")

if __name__ == '__main__':
    main()