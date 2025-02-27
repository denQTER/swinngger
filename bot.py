import random
import os
from telegram import Update
from telegram.ext import Application, CommandHandler, CallbackContext

# Путь к папке с фото
PHOTO_FOLDER = "photos"

# Функция для выбора случайного фото
async def send_random_photo(update: Update, context: CallbackContext):
    photo_list = [f for f in os.listdir(PHOTO_FOLDER) if f.lower().endswith((".png", ".jpg", ".jpeg"))]  # Фильтруем только изображения
    if not photo_list:  
        await update.message.reply_text("Нет доступных фото.")
        return

    photo_path = os.path.join(PHOTO_FOLDER, random.choice(photo_list))  
    with open(photo_path, "rb") as photo:
        # Отправляем фото с текстом в одном сообщении
        await update.message.reply_photo(photo, caption="Спасибо что вызвали волосатое чмо, можете полюбоваться мной перед тем как плюнуть в монитор")

# Основной код
def main():
    TOKEN = "7824019423:AAEcNqDqUzGxrSPbft13zH4M2FnoabEqDr8"

    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("swinngger_volosati_pidor", send_random_photo))

    print("Бот запущен...")
    app.run_polling()

if __name__ == "__main__":
    main()
