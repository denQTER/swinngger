import logging
import random
import os
from telegram import Update
from telegram.ext import Application, CommandHandler, CallbackContext, CallbackQueryHandler

# Настроим логирование
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
logger = logging.getLogger(__name__)

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
        await update.message.reply_photo(photo)

# Функция обработки ошибок
def error(update: Update, context: CallbackContext):
    """Логирование ошибок, вызвавших исключение"""
    logger.warning('Update "%s" caused error "%s"', update, context.error)

# Основной код
def main():
    TOKEN = "7824019423:AAEcNqDqUzGxrSPbft13zH4M2FnoabEqDr8"

    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("swinngger_volosati_pidor", send_random_photo))

    # Добавляем обработчик ошибок
    app.add_error_handler(error)

    print("Бот запущен...")
    app.run_polling()

if __name__ == "__main__":
    main()
