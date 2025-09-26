from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# توکن رباتت را اینجا قرار بده
BOT_TOKEN = "ت8272792867:AAGRALibbwMjgacL1E4QB827byav5tyKGoo"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("سلام! ربات آماده است.")

if __name__ == "__main__":
    # ساخت اپلیکیشن و اجرای Polling
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    
    # اضافه کردن Handler برای دستور /start
    app.add_handler(CommandHandler("start", start))
    
    # اجرای ربات
    app.run_polling()

