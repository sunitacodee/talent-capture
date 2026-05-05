from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager
from flask_marshmallow import Marshmallow

import logging
import os
# from flask_login import LoginManager

db = SQLAlchemy()
migrate = Migrate()
jwt = jwt = JWTManager()
ma= Marshmallow()

# login_manager = LoginManager()
# login_manager.login_view = "auth.login"



def setup_logging():
    if not os.path.exists("logs"):
        os.mkdir("logs")

    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s %(levelname)s %(name)s : %(message)s",
        handlers=[
            logging.FileHandler("logs/app.log"),  # 👈 FILE LOG
            logging.StreamHandler()              # 👈 TERMINAL LOG
        ]
    )