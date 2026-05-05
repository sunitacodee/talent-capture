from flask import Blueprint,request,jsonify
from app.models.user import User
from app.extensions import db
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.schemas.user_schema import users_schema
# from app.decorators import role_required
user_bp = Blueprint("user",__name__,url_prefix="/users")

@user_bp.route("/", methods=["GET"])
# @role_required('admin')
def getUsers():
    users = User.query.all()
    if users:
        return jsonify(users_schema.dump(users))
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