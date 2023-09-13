from flask import Blueprint

questions_bp = Blueprint("questions", __name__, url_prefix="/question")

@questions_bp.route("/")
def home_questions():
    return "hello question component"
