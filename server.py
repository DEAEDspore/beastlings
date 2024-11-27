import os
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello from Beastlings Server!"

if __name__ == '__main__':
    # Получение порта из переменной окружения или использование порта по умолчанию 5000
    port = int(os.environ.get('PORT', 5000))
    # Установка '0.0.0.0' для привязки ко всем интерфейсам
    app.run(host='0.0.0.0', port=port, debug=True)
