import logging
from flask import Flask
from telegram import Update
from telegram.ext import Application, CommandHandler, CallbackContext
import os

# Включаем логирование для отслеживания ошибок
logging.basicConfig(format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO)
logger = logging.getLogger(__name__)

# Создаем Flask-приложение
app = Flask(__name__)

# Токен вашего бота
TOKEN = "7824019423:AAHE2VH8Q1vDkLK9bceaKMPMhrzsSOdxY5Y"

# Путь к папке с фото
PHOTO_FOLDER = "photos"

# Функция для отправки случайного фото
async def send_random_photo(update: Update, context: CallbackContext):
    import random
    import os

    photo_list = [f for f in os.listdir(PHOTO_FOLDER) if f.lower().endswith((".png", ".jpg", ".jpeg"))]
    if not photo_list:
        await update.message.reply_text("Нет доступных фото.")
        return

    photo_path = os.path.join(PHOTO_FOLDER, random.choice(photo_list))
    with open(photo_path, "rb") as photo:
        await update.message.reply_photo(photo)

# Функция для обработки команды /start
async def start(update: Update, context: CallbackContext):
    await update.message.reply_text("Спасибо что вызвали волосатое чмо, можете полюбоваться мной перед тем как плюнуть в монитор")

# Функция для запуска бота
def start_bot():
    application = Application.builder().token(TOKEN).build()

    # Добавление команд
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("swinngger_volosati_pidor", send_random_photo))

    application.run_polling()

# Запуск Flask-приложения
@app.route('/')
def home():
    return "Flask-приложение работает!"

# Запуск приложения и бота
if __name__ == "__main__":
    from threading import Thread

    # Запуск бота в отдельном потоке
    bot_thread = Thread(target=start_bot)
    bot_thread.start()

    # Запуск Flask-приложения
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)), debug=True)
