import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, ContextTypes

# Токен твоего бота
TOKEN = '7745016365:AAEzYu3H7IhUOv0NcdZkIr2qf5eNC6T9JVc'

# Ссылка на сайт (игру)
SITE_URL = "https://deaedspore.github.io/beastlings/docs/"  # Текущая ссылка на GitHub Pages

# Функция для команды /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    # Создание кнопки с параметром web_app для мини-приложения
    keyboard = [
        [InlineKeyboardButton("Перейти в игру", web_app={'url': SITE_URL})]  # Мини-приложение Telegram
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    # Отправка сообщения с кнопкой
    await update.message.reply_text("Привет! Нажми кнопку ниже, чтобы перейти в игру:", reply_markup=reply_markup)

def main():
    # Настройка логирования
    logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

    # Инициализация Application
    application = Application.builder().token(TOKEN).build()

    # Добавляем обработчик команды /start
    application.add_handler(CommandHandler('start', start))

    # Запуск бота
    application.run_polling()

if __name__ == '__main__':
    main()
