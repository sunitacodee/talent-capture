from flask import Blueprint,request,jsonify
from werkzeug.security import generate_password_hash,check_password_hash
from app.models.user import User
from app.extensions import db
import logging
from flask_jwt_extended import create_access_token

auth_bp = Blueprint('__auth__',__name__,url_prefix="/auth")
logger = logging.getLogger(__name__)
@auth_bp.route('/register',methods=["POST"])
def register():
    try:
        data= request.json
        logger.info(data)       
        
        logger.info(f"Register request: {data}")

        user = User(
            username=data["username"],
            email   =data["email"],
            password=generate_password_hash(data["password"]),
            first_name=data["first_name"],
            last_name=data["last_name"],
            user_type=data["user_type"]

            )
        db.session.add(user)
        db.session.commit()
        return jsonify({"message":"user registered successfully"})
    except Exception as e:
        logger.error(f"Error occurred: {str(e)}")
        return {"error": f"Error occurred: {str(e)}"}, 500
    

@auth_bp.route("/login",methods=["POST"])
def login():
    try:
         data= request.json
         user = User.query.filter_by(email=data["email"]).first()
         if not user or not check_password_hash(user.password,data["password"]):
             return jsonify({"error": "Invalid credentials"}),401
         
         token = create_access_token(
             identity=str(user.email),
              additional_claims={
        "role": user.user_type
    }
                                     )
         return jsonify({
              "message": "Login successful",
               "access_token": token
         })

    except Exception as e:
        logger.error(f"Error occurred: {str(e)}")
        return {"error": "Something went wrong could not login"}, 500