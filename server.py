from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = "supersecretkey"

# Роут для экрана загрузки
@app.route("/")
def loading_screen():
    return render_template("loading.html")

# Роут для выбора первого бистлинга
@app.route("/select_beastling")
def select_beastling():
    beastlings = [1, 2, 3]  # Идентификаторы ваших бистлингов
    return render_template("select_beastling.html", beastlings=beastlings)

# Роут для сохранения выбора игрока
@app.route("/save_beastling", methods=["POST"])
def save_beastling():
    selected_beastling = request.form.get("beastling")
    session["player_beastling"] = selected_beastling
    return redirect(url_for("battle"))

# Роут для боя
@app.route("/battle")
def battle():
    player_beastling = session.get("player_beastling")
    return render_template("battle.html", player_beastling=player_beastling)

# Роут для завершения боя
@app.route("/battle_end", methods=["POST"])
def battle_end():
    result = request.form.get("result")  # "win" или "lose"
    session["last_battle_result"] = result
    return redirect(url_for("main_menu"))

# Роут для главного меню
@app.route("/main_menu")
def main_menu():
    player_beastling = session.get("player_beastling")
    last_battle_result = session.get("last_battle_result", "none")
    return render_template("main_menu.html", player_beastling=player_beastling, last_battle_result=last_battle_result)

if __name__ == "__main__":
    app.run(debug=True)
