import os
import sys
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters

BOT_TOKEN = os.environ.get("BOT_TOKEN")
OWNER_ID = os.environ.get("OWNER_ID")

if not BOT_TOKEN:
    print("❌ BOT_TOKEN environment variable is missing")
    sys.exit(1)

print("✅ Starting bot with token loaded...")

async def start(update, context):
    await update.message.reply_text("سلام! من رباتم 😊")

async def echo(update, context):
    await update.message.reply_text(update.message.text)

if __name__ == '__main__':
    print("🚀 Bot started, polling Telegram…")
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))
    app.run_polling()
