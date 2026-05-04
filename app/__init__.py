from flask import Flask
from flask_migrate import Migrate

from .extensions import db, migrate 
# login_manager
from .routes.user import user_bp
from app.models.user import User

# from .routes.product import product_bp

migrate = Migrate()

def create_app():
    app = Flask(__name__)
    app.config.from_object("app.config.Config")

    db.init_app(app)
    migrate.init_app(app, db)
    
    # login_manager.init_app(app)

    app.register_blueprint(user_bp)
    # app.register_blueprint(product_bp)

    return app