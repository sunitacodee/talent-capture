from flask import Blueprint,request,jsonify
from app.models.user import User
from app.extensions import db
from flask_jwt_extended import jwt_required, get_jwt_identity,get_jwt
from app.schemas.user_schema import users_schema
from app.decorators.role_required import role_required
from flask import current_app
user_bp = Blueprint("user",__name__)

@user_bp.route("/me", methods=["GET"],strict_slashes=False)
# @jwt_required()
@role_required('admin','employee','employer')
def getAuthUser():
    try:
        email = get_jwt_identity()
        user = User.query.filter_by(email=email).first()
        return jsonify(user.to_dict())
    except Exception as e:
        current_app.logger.exception(f"error fetching users : {str(e)}")      
        return jsonify(f"error fetching users : {str(e)}")


@user_bp.route("/", methods=["GET"])
@role_required('admin','employee','employer')
def getUsers():
    try:
        users = User.query.all()      
        if users:
            return jsonify(users_schema.dump(users))
        return jsonify("no users found")
    except Exception as e:
        current_app.logger.info(f"error fetching users : {str(e)}")      
        return jsonify(f"error fetching users : {str(e)}")  

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
        current_app.logger.info(f"error deleting user : {str(e)}")      
        return jsonify(f"error deleting user : {str(e)}")