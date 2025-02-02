from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import CallbackContext

# მენიუს ღილაკები
menu_keyboard = [
    ["ℹ ინფორმაცია", "📞 კონტაქტი"],
    ["🔄 გამეორება"]
]
menu_markup = ReplyKeyboardMarkup(menu_keyboard, resize_keyboard=True)

async def start(update: Update, context: CallbackContext):
    user = update.message.from_user
    await update.message.reply_text(f"გამარჯობა, {user.first_name}! 😊", reply_markup=menu_markup)

async def help_command(update: Update, context: CallbackContext):
    await update.message.reply_text("📌 ბრძანებები:\n/start - ბოტის დაწყება\n/help - დახმარება")

async def echo(update: Update, context: CallbackContext):
    text = update.message.text
    if text == "ℹ ინფორმაცია":
        await update.message.reply_text("ეს არის სატესტო ბოტი! 🤖")
    elif text == "📞 კონტაქტი":
        await update.message.reply_text("📧 Email: example@example.com\n📞 ტელ: +995 555 123 456")
    elif text == "🔄 გამეორება":
        await update.message.reply_text("🔄 აი, ვიმეორებ! 😃")
    else:
        await update.message.reply_text(f"თქვენ თქვით: {text}")
