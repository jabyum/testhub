from flask_form import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired

# Форма публикации вопросов
class QuestionForm(FlaskForm):
    question_header = StringField("Заголовок", validators=[DataRequired("обязательно")])
    question_text = TextAreaField("Опиши проблему", validators=[DataRequired("обязательно")])
    button = SubmitField("Опубликовать")
# форма для ответа
class AnswerForm(FlaskForm):
    answer_text = TextAreaField("Ответ на вопрос", validators=[DataRequired("обязательно")])
    button = SubmitField("Ответить")
# login
class LoginRegisterForm(FlaskForm):
    email = StringField("Почта", validators=[DataRequired()])
    password = StringField("Пароль", validators=[DataRequired()])
    button = SubmitField("Войти/Зарегистрироваться")

