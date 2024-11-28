import os
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/loading')
def loading():
    return render_template('index.html')  # Убедитесь, что index.html существует в папке templates

@app.route('/choose')
def choose():
    return render_template('choose.html')  # Убедитесь, что choose.html существует в папке templates

@app.route("/battle")
def battle():
    player_beastling = request.args.get('beastling', 1, type=int)
    return render_template("battle.html", player_beastling=player_beastling)

@app.route("/main_menu")
def main_menu():
    return render_template("main_menu.html", player_beastling=player_beastling)

if __name__ == "__main__":
    # Используем порт из переменной окружения
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)
