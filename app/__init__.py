from flask import Flask
from .extensions import db, migrate ,mail
from .routes.user import user_bp
from .routes.auth import auth_bp
from app.models.user import User
from app.models.employee import Employee
from app.models.employer import Employer
from app.models.province import Province
from app.models.district import District
from app.models.localbody import LocalBody
from app.models.localBodyWard import LocalBodyWard
from app.models.userVerificationCodes import UserVerificationCodes
from app.extensions import jwt
from app.decorators import role_required
import logging
from logging.handlers import RotatingFileHandler
from app.routes.employee import employee_bp
from app.routes.userProfile import user_profile_bp
from app.commands import address_seeder
from app.routes.location import location_bp
from flask_cors import CORS
from flask import request
import os
def create_app():
    app = Flask(__name__)
    app.config.from_object("app.config.Config")

    CORS(
    app,
    supports_credentials=True,
    origins=[
       os.getenv("FRONTEND_URL"),
        "http://127.0.0.1:5173"
    ]
)
    

    @app.before_request
    def handle_preflight():
        if request.method == "OPTIONS":
            return {}, 200 

    @app.route("/")
    def test():
        return "Hello talent capturexamp"

    jwt.init_app(app)

    db.init_app(app)
    migrate.init_app(app, db)
    #config mailer
    mail.init_app(app)
    #app 

    #register commands here
    app.cli.add_command(address_seeder)   


    CORS(auth_bp, origins=["http://localhost:5173"], supports_credentials=True)
    
    app.register_blueprint(auth_bp,url_prefix="/api/auth")
    CORS(user_bp, origins=["http://localhost:5173",""], supports_credentials=True)

    #register  routes here
    app.register_blueprint(user_bp,url_prefix="/api/users")
    app.register_blueprint(user_profile_bp,url_prefix="/api/users/profile")
    app.register_blueprint(employee_bp, url_prefix="/api/employees")
    app.register_blueprint(location_bp,url_prefix="/api/locations")


    handler = RotatingFileHandler('app.log', maxBytes=10000, backupCount=3)
    handler.setLevel(logging.INFO)

    formatter = logging.Formatter(
        '%(asctime)s %(levelname)s: %(message)s'
    )
    handler.setFormatter(formatter)

    app.logger.addHandler(handler)
    app.logger.setLevel(logging.INFO)

    return app