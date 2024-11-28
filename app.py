from flask import Flask, render_template, request, jsonify
import random

app = Flask(__name__)

# Бистлинги
BEASTLINGS = [
    {"name": "Beastling 1", "image": "beastling1.png"},
    {"name": "Beastling 2", "image": "beastling2.png"},
    {"name": "Beastling 3", "image": "beastling3.png"},
]

@app.route("/")
def loading_page():
    """Страница загрузки."""
    return render_template("loading.html")

@app.route("/choose", methods=["GET", "POST"])
def choose_beastling():
    """Выбор стартового бистлинга."""
    if request.method == "POST":
        selected = int(request.form["beastling"])
        return render_template("battle.html", player_beastling=BEASTLINGS[selected])
    return render_template("choose.html", beastlings=BEASTLINGS)

@app.route("/battle", methods=["POST"])
def battle():
    """Бой между игроком и ботом."""
    player_choice = request.json["choice"]
    bot_choice = random.choice(["rock", "scissors", "paper"])
    result = determine_winner(player_choice, bot_choice)
    return jsonify({"result": result, "bot_choice": bot_choice})

def determine_winner(player, bot):
    outcomes = {
        ("rock", "scissors"): "win",
        ("scissors", "paper"): "win",
        ("paper", "rock"): "win",
        ("scissors", "rock"): "lose",
        ("paper", "scissors"): "lose",
        ("rock", "paper"): "lose",
    }
    return outcomes.get((player, bot), "draw")

@app.route("/menu")
def menu_page():
    """Главное меню."""
    return render_template("menu.html")

if __name__ == "__main__":
    import os
    # Настройка порта для развертывания на Heroku
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)
