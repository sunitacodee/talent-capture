from flask import Blueprint,request,jsonify
from app.models.user import User
from app.extensions import db
from flask_jwt_extended import jwt_required, get_jwt_identity

user_bp = Blueprint("user",__name__,url_prefix="/users")

@user_bp.route("/", methods=["GET"])
def getUsers():
    users = User.query.all()
    if users:
        return User.__dict__
    return jsonify("no users found")

@user_bp.route("/<int:id>", methods=["DELETE"])
@jwt_required()
def deleteUser(id):
    try:
        user = User.query.get(id)
        if user:
            db.session.delete(user)
            db.session.commit()
            return jsonify("user deleted successfully")
        return jsonify("no users found")
    except Exception as  e :        
        return jsonify(f"error deleting user : {str(e)}")