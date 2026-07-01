from flask import Blueprint,request,jsonify
from werkzeug.security import generate_password_hash,check_password_hash
from app.models.user import User
from app.extensions import db
from flask_jwt_extended import create_access_token
from flask import current_app
from app.services.userService import UserService
auth_bp = Blueprint('__auth__',__name__)
from app.mailer.mailer import Mailer
@auth_bp.route('/register',methods=["POST"])
def register():
    try:
        data= request.json
        current_app.logger.info(data)      
        
        current_app.logger.info(f"Register request: {data}")

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
        verificationCode = UserService.generateUserVerifcationCode(user.id,'email_verification_code',300)
        Mailer.sendNotificationEmail(user.email,f"User registratered successfully", f"Your verification code is {verificationCode['code']}. "
        f"This code will expire in 5 minutes.")
        return jsonify({"message":"user registered successfully"})
    except Exception as e:
        current_app.logger.error(f"Error occurred: {str(e)}")
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
               "access_token": token,
               "user":user.to_dict()
         })

    except Exception as e:
        current_app.logger.error(f"Error occurred: {str(e)}")
        return {"error":f"Error occurred: {str(e)}"}, 500
    
