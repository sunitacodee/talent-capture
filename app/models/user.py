from datetime import datetime
from app.extensions import db
import uuid
from app.extensions import db
from flask_login import UserMixin

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)

    username = db.Column(db.String(100), unique=True, nullable=False)
    email = db.Column(db.String(150), unique=True, nullable=False)

    first_name = db.Column(db.String(100))
    last_name = db.Column(db.String(100))

    password = db.Column(db.String(255), nullable=False)

    # User type (admin, user, etc.)
    user_type = db.Column(db.String(50), default='user')

    # Auth / Security
    is_active = db.Column(db.Boolean, default=True)
    is_verified = db.Column(db.Boolean, default=False)

    login_token = db.Column(db.String(255), unique=True, nullable=True)

    # Timestamps
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    verified_at = db.Column(db.DateTime, nullable=True)
    last_logged_in = db.Column(db.DateTime, nullable=True)

    # Optional: soft delete
    deleted_at = db.Column(db.DateTime, nullable=True)

    # Helper method to generate token
    def generate_token(self):
        self.login_token = str(uuid.uuid4())

    # Convert to JSON (for API response)
    def to_dict(self):
        return {
            "id": self.id,
            "username": self.username,
            "email": self.email,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "user_type": self.user_type,
            "is_active": self.is_active,
            "is_verified": self.is_verified,
            "created_at": self.created_at,
            "updated_at": self.updated_at,
            "last_logged_in": self.last_logged_in
        }