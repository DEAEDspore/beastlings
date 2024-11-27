from telegram import Update, WebAppInfo, ReplyKeyboardMarkup, KeyboardButton
from telegram.ext import Application, CommandHandler
import logging

# Вставьте ваш токен бота сюда
TOKEN = "7745016365:AAEzYu3H7IhUOv0NcdZkIr2qf5eNC6T9JVc"
WEB_APP_URL = "https://beastlings-server-71968ef4b3d1.herokuapp.com/loading" # URL веб-приложения

# Логирование для отладки
logging.basicConfig(level=logging.INFO)

# Команда /start
async def start(update: Update, context):
    # Создаем кнопку с WebAppInfo
    button = KeyboardButton(text="Запустить игру", web_app=WebAppInfo(url=WEB_APP_URL))
    
    # Добавляем кнопку в клавиатуру
    keyboard = [[button]]
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)

    # Отправляем сообщение с клавиатурой
    await update.message.reply_text(
        "Нажмите кнопку ниже, чтобы начать игру:",
        reply_markup=reply_markup
    )

# Запуск бота
def main():
    # Создаем приложение
    app = Application.builder().token(TOKEN).build()

    # Обрабатываем команду /start
    app.add_handler(CommandHandler("start", start))

    # Запускаем бота
    app.run_polling()

if __name__ == "__main__":
    main()
