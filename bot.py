import random
import os
from telegram import Update
from telegram.ext import Application, CommandHandler, CallbackContext
import logging

# Логирование
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Получаем токен из переменных окружения
TOKEN = os.getenv("7824019423:AAEcNqDqUzGxrSPbft13zH4M2FnoabEqDr8")
PORT = int(os.environ.get("PORT", 8443))

# Папка с фото
PHOTO_FOLDER = "photos"

# Функция для отправки случайного фото
async def send_random_photo(update: Update, context: CallbackContext):
    photo_list = [f for f in os.listdir(PHOTO_FOLDER) if f.lower().endswith((".png", ".jpg", ".jpeg"))]
    if not photo_list:
        await update.message.reply_text("Нет доступных фото.")
        return

    photo_path = os.path.join(PHOTO_FOLDER, random.choice(photo_list))
    with open(photo_path, "rb") as photo:
        await update.message.reply_photo(photo, caption="Вот твоя картинка, Волосатый Пидор!")

# Создаём бота
app = Application.builder().token(TOKEN).build()
app.add_handler(CommandHandler("swinngger_volosati_pidor", send_random_photo))

# Запуск вебхука
async def main():
    logger.info("Бот запущен...")
    await app.bot.set_webhook(url=f"https://{os.environ['RENDER_EXTERNAL_HOSTNAME']}/{TOKEN}")
    await app.run_webhook(
        listen="0.0.0.0",
        port=PORT,
        url_path=TOKEN
    )

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
