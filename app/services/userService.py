from app.models.userProfile import UserProfile
from app.models.user import User
from app.validations.userValidator import validateUserProfile
import uuid
import os
from app.extensions import db
from werkzeug.utils import secure_filename

UPLOAD_FOLDER_PROFILE = "uploads/profile_pics"
UPLOAD_FOLDER_CV = "uploads/cvs"

os.makedirs(UPLOAD_FOLDER_PROFILE, exist_ok=True)
os.makedirs(UPLOAD_FOLDER_CV, exist_ok=True)

class UserService:
    @staticmethod
    def uploadUserProfile(profile_pic,user:User,profile:UserProfile)-> tuple[dict | None, list[str]]:

        errors =validateUserProfile(profile_pic)
        if errors:
            return None, errors

        filename = f"{uuid.uuid4()}_{secure_filename(profile_pic.filename)}"

        filepath = os.path.join(
        UPLOAD_FOLDER_PROFILE,
        filename
        )

        profile_pic.save(filepath)

        profile.profile_pic = filepath
        db.session.add(profile)
        db.session.commit()
        return profile.to_dict(),[]