import logging
import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes

BOT_TOKEN = os.environ.get("BOT_TOKEN", "8336349505:AAEKJ5aQcKX8jipXdby2OwnR5DKTl7Cu6FM")

logging.basicConfig(format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    await update.message.reply_text(f"Halo, {user.first_name}! Ketik /help untuk melihat perintah.")

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Daftar Perintah:\n\n"
        "/start - Mulai bot\n"
        "/help - Tampilkan bantuan\n"
        "/info - Info bot\n"
        "/hitung angka1 angka2 - Jumlahkan dua angka\n"
        "/echo pesan - Ulangi pesan\n"
        "/waktu - Tampilkan waktu sekarang"
    )

async def info(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Bot Telegram Syarif - dibuat dengan Python.")

async def hitung(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        if len(context.args) != 2:
            await update.message.reply_text("Contoh: /hitung 10 5")
            return
        a, b = float(context.args[0]), float(context.args[1])
        await update.message.reply_text(f"{a} + {b} = {a + b}")
    except ValueError:
        await update.message.reply_text("Masukkan angka yang valid!")

async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if context.args:
        await update.message.reply_text(" ".join(context.args))
    else:
        await update.message.reply_text("Contoh: /echo Halo!")

async def waktu(update: Update, context: ContextTypes.DEFAULT_TYPE):
    from datetime import datetime
    import pytz
    now = datetime.now(pytz.timezone("Asia/Jakarta"))
    await update.message.reply_text(f"{now.strftime('%A, %d %B %Y - %H:%M:%S WIB')}")

async def tidak_dikenal(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Ketik /help untuk melihat perintah.")

if __name__ == "__main__":
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(CommandHandler("info", info))
    app.add_handler(CommandHandler("hitung", hitung))
    app.add_handler(CommandHandler("echo", echo))
    app.add_handler(CommandHandler("waktu", waktu))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, tidak_dikenal))
    print("Bot berjalan...")
    app.run_polling()
