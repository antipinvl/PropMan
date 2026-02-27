from flask import Flask, request, redirect, url_for

import os

app = Flask(__name__)

# временное хранилище пользователей (как у тебя в проекте)
users = []

@app.route("/")
def home():
    return """
    <h1>Главная страница</h1>
    <p><a href="/register">Регистрация</a></p>
    <p><a href="/users">Список пользователей</a></p>
    """

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        name = request.form.get("name")
        email = request.form.get("email")
        role = request.form.get("role")

        users.append({
            "name": name,
            "email": email,
            "role": role
        })

        return redirect(url_for("users_list"))

    return """
    <h1>Регистрация пользователя</h1>
    <form method="POST">
        <input name="name" placeholder="Имя"><br>
        <input name="email" placeholder="Email"><br>
        <input name="role" placeholder="Роль"><br>
        <button type="submit">Зарегистрировать</button>
    </form>
    """

@app.route("/users")
def users_list():
    html = "<h1>Список пользователей</h1>"

    for u in users:
        html += f"<p>{u['name']} - {u['email']} - {u['role']}</p>"

    html += '<p><a href="/">На главную</a></p>'
    return html


# ❗️ ВАЖНО ДЛЯ RENDER
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)