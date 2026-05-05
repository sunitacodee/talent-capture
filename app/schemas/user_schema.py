from app.extensions import ma
from app.models.user import User

class UserSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = User
        load_instance = True
        exclude = ("password","verified_at","login_token","login_token",) 

user_schema = UserSchema()
users_schema = UserSchema(many=True)