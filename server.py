import os
import random
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    # Возвращаем HTML-файл
    return render_template('index.html')

@app.route('/play')
def play():
    # Получаем выбор игрока
    player_choice = request.args.get('choice')
    # Возможные варианты
    choices = ['rock', 'paper', 'scissors']
    bot_choice = random.choice(choices)
    
    # Логика игры
    if player_choice == bot_choice:
        result = "It's a draw!"
    elif (player_choice == 'rock' and bot_choice == 'scissors') or \
         (player_choice == 'scissors' and bot_choice == 'paper') or \
         (player_choice == 'paper' and bot_choice == 'rock'):
        result = "You win!"
    else:
        result = "You lose!"

    # Возвращаем результат в формате JSON
    return jsonify({
        'player_choice': player_choice,
        'bot_choice': bot_choice,
        'result': result
    })

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
