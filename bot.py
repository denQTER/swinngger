import os
import random
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, CallbackContext

# Папка с фото
PHOTO_FOLDER = "photos"

# Функция для отправки случайного фото с текстом
async def send_random_photo(update: Update, context: CallbackContext):
    photo_list = [f for f in os.listdir(PHOTO_FOLDER) if f.lower().endswith((".png", ".jpg", ".jpeg"))]
    
    if not photo_list:
        await update.message.reply_text("Нет доступных фото.")
        return
    
    photo_path = os.path.join(PHOTO_FOLDER, random.choice(photo_list))
    with open(photo_path, "rb") as photo:
        await update.message.reply_photo(photo, caption="Спасибо что вызвали волосатое чмо, можете полюбоваться мной перед тем как плюнуть в монитор")

# Функция старта
async def start(update: Update, context: CallbackContext):
    await update.message.reply_text("Привет! Напиши /swinngger_volosati_pidor, чтобы получить случайное фото.")

# Основной код
def main():
    TOKEN = "7824019423:AAEcNqDqUzGxrSPbft13zH4M2FnoabEqDr8"  # Вставь сюда новый токен!

    app = Application.builder().token(TOKEN).build()
    
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("swinngger_volosati_pidor", send_random_photo))

    print("Бот запущен...")
    app.run_polling(allowed_updates=Update.ALL_TYPES)

if __name__ == "__main__":
    main()
