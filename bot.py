from telegram import Bot, Update, InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes

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

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Обработчик команды /help."""
    await update.message.reply_text("Напишите /start, чтобы начать игру.")

app = Application.builder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("help", help_command))

if __name__ == "__main__":
    app.run_polling()
