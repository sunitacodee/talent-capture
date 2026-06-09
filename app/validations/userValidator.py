import os
import uuid
from flask import request, jsonify
from werkzeug.utils import secure_filename
from flask_jwt_extended import jwt_required, get_jwt_identity

from app import db
from app.models.user import User
from app.models.userProfile import UserProfile


ALLOWED_IMAGE_TYPES = [
    "image/jpeg",
    "image/jpg",
    "image/png",
    "image/webp"
]

ALLOWED_CV_TYPES = [
    "application/pdf"
]

MAX_PROFILE_SIZE = 2 * 1024 * 1024      # 2 MB
MIN_PROFILE_SIZE = 10 * 1024            # 10 KB

MAX_CV_SIZE = 5 * 1024 * 1024           # 5 MB
MIN_CV_SIZE = 20 * 1024                 # 20 KB


ALLOWED_EXTENSIONS = {"png", "jpg", "jpeg", "webp"}


def validateUserProfile(profile_pic):

    errors=[]
    # Validate mime type
    if profile_pic.mimetype not in ALLOWED_IMAGE_TYPES:
        errors.append(" Only jpg, jpeg, png, webp images are allowed")

    # Validate size
    profile_pic.seek(0, os.SEEK_END)
    file_size = profile_pic.tell()
    profile_pic.seek(0)

    if file_size > MAX_PROFILE_SIZE:
        errors.append(" Profile picture max size is 2 MB")

    if file_size < MIN_PROFILE_SIZE:
        errors.append(" Profile picture too small")
    extension = profile_pic.filename.rsplit(".", 1)[1].lower()

    if extension not in ALLOWED_EXTENSIONS:
        errors.append("Invalid file extension")

    return errors
           
def validateCv():

    # ==========================================
    # CV VALIDATION
    # ==========================================

    cv = request.files.get("cv")

    if cv:

        # Validate mime type
        if cv.mimetype not in ALLOWED_CV_TYPES:
            return jsonify({
                "message": "Only PDF files are allowed"
            }), 400

        # Validate size
        cv.seek(0, os.SEEK_END)
        file_size = cv.tell()
        cv.seek(0)

        if file_size > MAX_CV_SIZE:
            return jsonify({
                "message": "CV max size is 5 MB"
            }), 400

        if file_size < MIN_CV_SIZE:
            return jsonify({
                "message": "CV file too small"
            }), 400

        # Generate unique filename
        filename = f"{uuid.uuid4()}_{secure_filename(cv.filename)}"

        filepath = os.path.join(
            UPLOAD_FOLDER_CV,
            filename
        )

        cv.save(filepath)

        UserProfile.cv = filepath

    db.session.add(UserProfile)
    db.session.commit()

    return jsonify({
        "message": "Profile updated successfully",
        "data": UserProfile.to_dict()
    }), 200

   