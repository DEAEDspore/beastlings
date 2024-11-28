from flask import Flask, render_template, request, random, redirect, url_for, session

app = Flask(__name__)
app.secret_key = "supersecretkey"

@app.route("/")
def loading_screen():
    return render_template("loading.html")

@app.route("/select_beastling")
def select_beastling():
    beastlings = [
        {"id": 1, "name": "Fire Beastling", "image": "beastling1.png"},
        {"id": 2, "name": "Water Beastling", "image": "beastling2.png"},
        {"id": 3, "name": "Earth Beastling", "image": "beastling3.png"}
    ]
    return render_template("select_beastling.html", beastlings=beastlings)

@app.route("/save_beastling", methods=["POST"])
def save_beastling():
    selected_beastling = request.form.get("beastling")
    session["player_beastling"] = selected_beastling
    session["player_score"] = 0
    session["bot_score"] = 0
    return redirect(url_for("battle"))

@app.route("/battle")
def battle():
    player_beastling = session.get("player_beastling")
    if not player_beastling:
        return redirect(url_for("select_beastling"))
    return render_template("battle.html", player_beastling=player_beastling)

@app.route("/play_turn", methods=["POST"])
def play_turn():
    choices = ["rock", "paper", "scissors"]
    player_choice = request.form.get("choice")
    bot_choice = random.choice(choices)

    # Determine the result
    result = None
    if player_choice == bot_choice:
        result = "draw"
    elif (player_choice == "rock" and bot_choice == "scissors") or \
         (player_choice == "scissors" and bot_choice == "paper") or \
         (player_choice == "paper" and bot_choice == "rock"):
        result = "win"
        session["player_score"] += 1
    else:
        result = "lose"
        session["bot_score"] += 1

    # Check for game over
    if session["player_score"] == 3 or session["bot_score"] == 3:
        return redirect(url_for("battle_end"))

    return render_template("battle.html", player_choice=player_choice, bot_choice=bot_choice, result=result,
                           player_score=session["player_score"], bot_score=session["bot_score"])

@app.route("/battle_end")
def battle_end():
    player_score = session.get("player_score", 0)
    bot_score = session.get("bot_score", 0)
    session["player_score"] = 0
    session["bot_score"] = 0
    result = "win" if player_score > bot_score else "lose"
    return render_template("battle_end.html", result=result)

@app.route("/main_menu")
def main_menu():
    player_beastling = session.get("player_beastling")
    if not player_beastling:
        return redirect(url_for("select_beastling"))
    return render_template("main_menu.html", player_beastling=player_beastling)

if __name__ == "__main__":
    # Настраиваем запуск на определённом хосте и порту
    port = int(os.environ.get("PORT", 5000))  # Используем порт из переменной окружения, если указан
    app.run(host="0.0.0.0", port=port, debug=True)

