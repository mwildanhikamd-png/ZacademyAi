import os
import nest_asyncio
nest_asyncio.apply()

from telegram.ext import ApplicationBuilder, CommandHandler

TOKEN = os.environ.get("BOT_TOKEN")

async def start(update, context):
    await update.message.reply_text("Bot aktif 🚀")

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))

app.run_polling()
