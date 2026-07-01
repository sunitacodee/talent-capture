from app.models.userProfile import UserProfile
from app.models.user import User
from app.validations.userValidator import validateUserProfile
import uuid
import os
from app.extensions import db
from werkzeug.utils import secure_filename
from app.models.userVerificationCodes import UserVerificationCodes
UPLOAD_FOLDER_PROFILE = "uploads/profile_pics"
UPLOAD_FOLDER_CV = "uploads/cvs"

os.makedirs(UPLOAD_FOLDER_PROFILE, exist_ok=True)
os.makedirs(UPLOAD_FOLDER_CV, exist_ok=True)
from app.utils.utils import Utils
from datetime import datetime,timedelta
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
    
    def generateUserVerifcationCode(user_id:int,codeType,lifeInSec=600):
        code = Utils.generate_verification_code()
        current_time = datetime.now()
        expiration_time = current_time + timedelta(seconds=lifeInSec)

        verifcationCodeData  = UserVerificationCodes(user_id=user_id,
            code=code,
            type=codeType,
            life_in_sec=lifeInSec,   
            expired_at = expiration_time
            )
        db.session.add(verifcationCodeData)
        db.session.commit()
        return verifcationCodeData.to_dict()


