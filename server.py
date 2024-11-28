import os
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/loading')
def loading():
    return render_template('index.html')  # Убедитесь, что index.html существует в папке templates

@app.route('/choose')
def choose():
    return render_template('choose.html')  # Убедитесь, что choose.html существует в папке templates

if __name__ == "__main__":
    # Используем порт из переменной окружения
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)
