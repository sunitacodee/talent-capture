# from app import db
# from datetime import datetime


# class UserProfile(db.Model):
#     __tablename__ = "user_profiles"

#     id = db.Column(db.Integer, primary_key=True)

#     user_id = db.Column(
#         db.Integer,
#         db.ForeignKey("users.id"),
#         nullable=False,
#         unique=True
#     )

#     profile_pic = db.Column(db.String(255), nullable=True)

#     cv = db.Column(db.String(255), nullable=True)

#     created_at = db.Column(db.DateTime, default=datetime.utcnow)

#     updated_at = db.Column(
#         db.DateTime,
#         default=datetime.utcnow,
#         onupdate=datetime.utcnow
#     )

#     user = db.relationship("User", backref="profile")

#     def to_dict(self):
#         return {
#             "id": self.id,
#             "user_id": self.user_id,
#             "profile_pic": self.profile_pic,
#             "cv": self.cv
#         }


from app import db
from datetime import datetime
from sqlalchemy import UniqueConstraint 


class UserProfile(db.Model):
    __tablename__ = "user_profiles"

    id = db.Column(db.Integer, primary_key=True)

    user_id = db.Column(
        db.Integer,
        db.ForeignKey("users.id", ondelete="CASCADE"),
        nullable=False
    )

    profile_pic = db.Column(db.String(255), nullable=True)
    cv = db.Column(db.String(255), nullable=True)

    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(
        db.DateTime,
        default=datetime.utcnow,
        onupdate=datetime.utcnow
    )

    user = db.relationship("User", backref=db.backref("profile", uselist=False))
    __table_args__ = (
        UniqueConstraint('user_id', name='uq_user_profiles_user_id'),
    )

    def to_dict(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "profile_pic": self.profile_pic,
            "cv": self.cv
        }