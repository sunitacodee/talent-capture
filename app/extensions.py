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
