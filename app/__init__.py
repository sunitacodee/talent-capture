from flask import Flask
from flask_migrate import Migrate

from .extensions import db, migrate 
# login_manager
from .routes.user import user_bp
from .routes.auth import auth_bp
from app.models.user import User
# from .routes.product import product_bp
from app.extensions import jwt
from app.decorators import role_required
import logging
from logging.handlers import RotatingFileHandler

migrate = Migrate()
# setup_logging()


def create_app():
    app = Flask(__name__)

    app.config.from_object("app.config.Config")
    jwt.init_app(app)

    db.init_app(app)
    migrate.init_app(app, db)

    # login_manager.init_app(app)

    app.register_blueprint(user_bp)
    app.register_blueprint(auth_bp)

    handler = RotatingFileHandler('app.log', maxBytes=10000, backupCount=3)
    handler.setLevel(logging.INFO)

    formatter = logging.Formatter(
        '%(asctime)s %(levelname)s: %(message)s'
    )
    handler.setFormatter(formatter)

    app.logger.addHandler(handler)
    app.logger.setLevel(logging.INFO)

    return app