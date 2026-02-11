import os
import nest_asyncio
nest_asyncio.apply()

from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# ===============================
# AMBIL TOKEN DARI RAILWAY
# ===============================
TOKEN = os.environ.get("BOT_TOKEN")

if not TOKEN:
    raise ValueError("BOT_TOKEN tidak ditemukan di environment variables.")

# ===============================
# COMMAND: /start
# ===============================
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Bot aktif 🚀")

# ===============================
# COMMAND: /help
# ===============================
async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "ZACADEMY AI BOT\n\n"
        "Perintah tersedia:\n"
        "/start - Cek bot aktif\n"
        "/help - Bantuan"
    )

# ===============================
# MAIN APP
# ===============================
app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("help", help_command))

print("Bot running...")
app.run_polling()
