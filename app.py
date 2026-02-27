from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Список пользователей
users_list = [
    {"id": 1, "name": "Юрий", "email": "yuri@mail.com", "role": "Арендатор", "reviews": []},
    {"id": 2, "name": "Елена", "email": "elena@mail.com", "role": "Арендодатель", "reviews": []}
]

# Главная страница
@app.route("/")
def index():
    return render_template("index.html")

# Страница регистрации пользователя
@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        name = request.form.get("name")
        email = request.form.get("email")
        role = request.form.get("role")

        if name and email and role:
            user_id = len(users_list) + 1
            users_list.append({
                "id": user_id,
                "name": name,
                "email": email,
                "role": role,
                "reviews": []
            })
            return redirect(url_for("users"))

    return render_template("register.html")

# Страница списка пользователей
@app.route("/users")
def users():
    return render_template("users.html", users=users_list)

# Страница профиля пользователя
@app.route("/profile/<int:user_id>")
def profile(user_id):
    user = next((u for u in users_list if u["id"] == user_id), None)
    if user:
        return render_template("profile.html", user=user)
    return redirect(url_for("users"))

# Добавление отзыва
@app.route("/add_review/<int:user_id>", methods=["POST"])
def add_review(user_id):
    user = next((u for u in users_list if u["id"] == user_id), None)

    if user:
        reviewer = request.form.get("reviewer")
        text = request.form.get("text")

        if reviewer and text:
            user["reviews"].append({
                "reviewer": reviewer,
                "text": text
            })

    return redirect(url_for("profile", user_id=user_id))


if __name__ == "__main__":
    app.run(debug=True)