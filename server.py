from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = "supersecretkey"

@app.route("/")
def loading_screen():
    return render_template("loading.html")

@app.route("/select_beastling")
def select_beastling():
    beastlings = ["1", "2", "3"]
    return render_template("select_beastling.html", beastlings=beastlings)

@app.route("/save_beastling", methods=["POST"])
def save_beastling():
    selected_beastling = request.form.get("beastling")
    session["player_beastling"] = selected_beastling
    return redirect(url_for("battle"))

@app.route("/battle")
def battle():
    player_beastling = session.get("player_beastling")
    if not player_beastling:
        return redirect(url_for("select_beastling"))
    return render_template("battle.html", player_beastling=player_beastling)

@app.route("/battle_end", methods=["POST"])
def battle_end():
    result = request.form.get("result")  # win or lose
    session["last_battle_result"] = result
    return redirect(url_for("main_menu"))

@app.route("/main_menu")
def main_menu():
    player_beastling = session.get("player_beastling")
    if not player_beastling:
        return redirect(url_for("select_beastling"))
    last_battle_result = session.get("last_battle_result", "none")
    return render_template("main_menu.html", player_beastling=player_beastling, last_battle_result=last_battle_result)

if __name__ == "__main__":
    app.run(debug=True)
