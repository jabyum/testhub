from flask import Blueprint

users_bp = Blueprint("users", __name__, url_prefix="/user")
# создать url
@users_bp.route("/")
def home_user():
    return "hello user component"

