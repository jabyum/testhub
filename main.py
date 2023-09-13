from flask import Flask
from questions import questions_bp
from users import users_bp
app = Flask(__name__)
app.config["CSRF_ENABLED"] = True
app.config["SECRET_KEY"] = "hard-to-find"
#регистрация компонентов
app.register_blueprint(questions_bp)
app.register_blueprint(users_bp)
@app.route("/")
def home():
    questions_link = "<a href='/question'>Вопросы</a><br>"
    user_links = "<a href='/user'>Пользователи</a><br>"
    return questions_link + user_links
#запуск
app.run(debug=True)