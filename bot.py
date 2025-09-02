from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes

# === Настройки ===
TOKEN = "8221164975:AAG3Mt4fXlDOP4wrNRE0fKtbKT0mje8B0jU"
GROUP_ID = -1002969346006  # ID вашей группы (отрицательное число для супергрупп)
START_TEXT = "Привет! Отправь боту фото твоего студенческого (или скриншот личного кабинета на lk.mirea.ru) и твой ник в Minecraft, чтобы мы могли добавить тебя на наш сервер"
HELP_TEXT = "Отправь боту фото твоего студенческого (или скриншот личного кабинета на lk.mirea.ru) и твой ник в Minecraft, чтобы мы могли добавить тебя на наш сервер. Канал сервера: @DoDozeMIREA"

# === Обработчики команд ===
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(START_TEXT)

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(HELP_TEXT)

# === Пересылка текстовых сообщений ===
async def forward_text(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text
    if text.strip().lower() not in ("/start", "/help"):
        await context.bot.send_message(chat_id=GROUP_ID, text=text)

# === Пересылка фото ===
async def forward_photo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # Берём последнее (наибольшее по качеству) фото
    photo = update.message.photo[-1]
    caption = update.message.caption if update.message.caption else ""
    await context.bot.send_photo(chat_id=GROUP_ID, photo=photo.file_id, caption=caption)

# === Запуск бота ===
def main():
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, forward_text))
    app.add_handler(MessageHandler(filters.PHOTO, forward_photo))

    print("Бот запущен...")
    app.run_polling()

main()

