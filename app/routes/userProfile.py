from flask import Blueprint,jsonify,request
from app.models.userProfile import UserProfile
from app.models.user import User
from flask_jwt_extended import jwt_required,get_jwt_identity
from werkzeug.utils import secure_filename
from app.services.userService import UserService
from flask import current_app
user_profile_bp = Blueprint('user_profile',__name__)



@user_profile_bp.route("/",methods = ["POST"])
@jwt_required()
def uploadUserProfile():
    try:
        email = get_jwt_identity()
        data = request.json
        user = User.query.filter(User.email == email).first()


        if not user:
            return jsonify({
                "message": f"User not found id : {email}"
            }), 404
        profile = UserProfile.query.filter_by(
            user_id=user.id
        ).first()

        if not profile:
            profile = UserProfile(user_id=user.id)
        profile_pic = request.files.get("profile_pic")

        if not profile_pic:
            return jsonify({
                "message": "No profile picture provided"
            }), 400            
        profile,errors=UserService.uploadUserProfile(profile_pic,user,profile)
        if errors:
            return jsonify({"errors": errors}), 422
        return jsonify({
                    "message": "Profile updated successfully",
                    "data": profile.to_dict()
                }), 200
          
    
    except Exception as e:
        current_app.logger.info(f"error uploading user profile: {str(e)}")      
        return jsonify(f"error uploading user profile pic : {str(e)}"),500


@user_profile_bp.route("/cv",methods = ["POST"])
@jwt_required()
def uploadUserCV():
    try:
        data = request.json
        user = get_jwt_identity()
        return "user cv upload code here"
    except Exception as e:
        current_app.logger.info(f"error uploading user profile: {str(e)}")      
        return jsonify(f"error uploading user profile pic : {str(e)}")

