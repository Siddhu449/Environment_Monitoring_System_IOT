
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes

# Command handler for the /start command
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    # Create a button linking to GitHub
    keyboard = [[InlineKeyboardButton("Visit My GitHub", url="https://github.com/kartos125?tab=projects")],
                [InlineKeyboardButton("I have visited GitHub", callback_data="visited_github")]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text("Welcome! Please visit my GitHub profile using the button below. "
                                    "Once you've done that, click the confirmation button.", reply_markup=reply_markup)

# Callback for button interactions
async def button_callback(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = update.callback_query
    await query.answer()  # Acknowledge the button click

    if query.data == "visited_github":
        # Send the YouTube link after user confirms visiting GitHub
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
    application.add_handler(CallbackQueryHandler(button_callback))

    # Start the bot
    application.run_polling()
    print("Bot is running...")

if __name__ == '__main__':
    main()
