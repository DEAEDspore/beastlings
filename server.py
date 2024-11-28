import os
import random
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Главная страница загрузки
@app.route('/')
def loading():
    return render_template('index.html')

# Выбор бистлинга
@app.route('/choose', methods=['GET', 'POST'])
def choose():
    beastlings = [
        {'id': '1', 'name': 'Бистлинг 1', 'image': '/static/images/beastling1.png'},
        {'id': '2', 'name': 'Бистлинг 2', 'image': '/static/images/beastling2.png'},
        {'id': '3', 'name': 'Бистлинг 3', 'image': '/static/images/beastling3.png'}
    ]
    if request.method == 'POST':
        player_beastling = request.form.get('beastling')
        if player_beastling:
            return redirect(url_for('battle', beastling=player_beastling))
    return render_template('choose.html', beastlings=beastlings)

# Логика боя
@app.route('/battle', methods=['GET', 'POST'])
def battle():
    player_beastling = request.args.get('beastling', default='1')
    player_score = int(request.args.get('player_score', 0))
    bot_score = int(request.args.get('bot_score', 0))

    if request.method == 'POST':
        player_choice = request.form.get('choice')
        bot_choice = random.choice(['rock', 'paper', 'scissors'])
        result = determine_winner(player_choice, bot_choice)

        if result == 'win':
            player_score += 1
        elif result == 'lose':
            bot_score += 1

        if player_score == 3 or bot_score == 3:
            result = 'win' if player_score == 3 else 'lose'
            return redirect(url_for('end_battle', result=result, beastling=player_beastling))

        return render_template(
            'battle.html',
            player_beastling=player_beastling,
            player_choice=player_choice,
            bot_choice=bot_choice,
            player_score=player_score,
            bot_score=bot_score
        )

    return render_template(
        'battle.html',
        player_beastling=player_beastling,
        player_score=player_score,
        bot_score=bot_score
    )

# Завершение боя
@app.route('/end_battle')
def end_battle():
    result = request.args.get('result')
    player_beastling = request.args.get('beastling')
    return render_template('end_battle.html', result=result, beastling=player_beastling)

# Главное меню
@app.route('/main_menu')
def main_menu():
    player_beastling = request.args.get('beastling', default='1')
    return render_template('main_menu.html', player_beastling=player_beastling)

# Определение победителя
def determine_winner(player, bot):
    if player == bot:
        return 'draw'
    elif (player == 'rock' and bot == 'scissors') or \
         (player == 'scissors' and bot == 'paper') or \
         (player == 'paper' and bot == 'rock'):
        return 'win'
    else:
        return 'lose'

# Запуск сервера
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)
