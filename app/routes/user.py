from flask import Blueprint,request,jsonify
from app.models.user import User
from app.extensions import db
user_bp = Blueprint("user",__name__,url_prefix="/users")

@user_bp.route("/", methods=["GET"])
def getUsers():
    users = User.query.all()
    if users:
        return jsonify("all users")
    return jsonify("no users found")