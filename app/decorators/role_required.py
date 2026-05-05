from functools import wraps
from flask_jwt_extended import jwt_required,get_jwt
from flask import jsonify

def role_required(*roles):
    def wrapper(fn):
        @wraps(fn)
        @jwt_required()
        def decorator(*args,**kwargs):
            claims = get_jwt()
            user_role = claims.get("role")

            if not user_role:
                return jsonify({"error": "Role missing in token"}),401
            
            if  user_role not in roles:
                return jsonify({
                    "error":"Forbidden",
                    "allowed_roles":roles
                      }),403
            return fn(*args,**kwargs)
        return decorator
    return wrapper