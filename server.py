import os
import random
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Главная страница загрузки
@app.route('/loading')
def loading():
    return render_template('index.html')  # Отображает страницу загрузки

# Выбор персонажа
@app.route('/choose', methods=['GET', 'POST'])
def choose():
    if request.method == 'POST':
        player_beastling = request.form.get('beastling')
        if player_beastling:
            return redirect(url_for('battle', beastling=player_beastling))
    return render_template('choose.html')

# Страница боя
@app.route('/battle', methods=['GET', 'POST'])
def battle():
    player_beastling = request.args.get('beastling', default='1')
    if request.method == 'POST':
        player_choice = request.form.get('choice')
        bot_choice = random.choice(['rock', 'paper', 'scissors'])
        result = determine_winner(player_choice, bot_choice)
        
        # Логика подсчёта побед/поражений
        player_score = int(request.args.get('player_score', 0))
        bot_score = int(request.args.get('bot_score', 0))

        if result == 'win':
            player_score += 1
        elif result == 'lose':
            bot_score += 1

        # Проверяем победу или поражение
        if player_score == 3:
            return redirect(url_for('end_battle', result='win', beastling=player_beastling))
        elif bot_score == 3:
            return redirect(url_for('end_battle', result='lose', beastling=player_beastling))

        # Обновляем данные для боя
        return render_template(
            'battle.html',
            player_beastling=player_beastling,
            player_choice=player_choice,
            bot_choice=bot_choice,
            player_score=player_score,
            bot_score=bot_score
        )

    return render_template('battle.html', player_beastling=player_beastling, player_score=0, bot_score=0)

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

# Функция для определения победителя
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
    # Настраиваем запуск на определённом хосте и порту
    port = int(os.environ.get("PORT", 5000))  # Используем порт из переменной окружения, если указан
    app.run(host="0.0.0.0", port=port, debug=True)
