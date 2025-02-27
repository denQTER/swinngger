import random
import os
from flask import Flask, request
from telegram import Update
from telegram.ext import Application, CommandHandler, CallbackContext

# Путь к папке с фото
PHOTO_FOLDER = "photos"

app = Flask(__name__)

# Функция для выбора случайного фото
async def send_random_photo(update: Update, context: CallbackContext):
    photo_list = [f for f in os.listdir(PHOTO_FOLDER) if f.lower().endswith((".png", ".jpg", ".jpeg"))]  # Фильтруем только изображения
    if not photo_list:
        await update.message.reply_text("Нет доступных фото.")
        return

    photo_path = os.path.join(PHOTO_FOLDER, random.choice(photo_list))
    with open(photo_path, "rb") as photo:
        await update.message.reply_photo(photo, caption="Спасибо что вызвали волосатое чмо, можете полюбоваться мной перед тем как плюнуть в монитор")

# Обработчик команды /swinngger_volosati_pidor
async def handle_command(update: Update, context: CallbackContext):
    await send_random_photo(update, context)

# Функция, которая будет запускать бота
def start_bot():
    TOKEN = "7824019423:AAHE2VH8Q1vDkLK9bceaKMPMhrzsSOdxY5Y"
    app_telegram = Application.builder().token(TOKEN).build()
    app_telegram.add_handler(CommandHandler("swinngger_volosati_pidor", handle_command))

    print("Бот запущен...")
    app_telegram.run_polling()

# Запуск приложения Flask
@app.route('/')
def hello():
    return "Бот работает на Flask и Render!"

if __name__ == "__main__":
    start_bot()
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
