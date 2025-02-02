from telegram.ext import Application, CommandHandler, MessageHandler, filters
from config import TOKEN
from modules.handlers import start, help_command, echo

def main():
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))

    print("✅ ბოტი გაშვებულია...")
    app.run_polling()

if __name__ == "__main__":
    main()
