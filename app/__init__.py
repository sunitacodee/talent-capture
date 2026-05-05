from flask import Flask
from flask_migrate import Migrate

from .extensions import db, migrate 
# login_manager
from .routes.user import user_bp
from .routes.auth import auth_bp
from app.models.user import User
# from .routes.product import product_bp
from app.extensions import jwt
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

    return app