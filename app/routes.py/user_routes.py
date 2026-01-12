from flask import Blueprint, jsonify

user_bp = Blueprint("user", __name__)

from flask import Blueprint, jsonify
from app.models.user import User

user_bp = Blueprint("user", __name__)

@user_bp.route("/users", methods=["GET"])
def get_users():
    users = User.query.all()
    return jsonify([{"id": u.id, "name": u.name, "email": u.email} for u in users])
