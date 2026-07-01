from app.extensions import db
from datetime import datetime
class UserVerificationCodes(db.Model):
    __tablename__ = 'user_verification_codes'
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id', ondelete='RESTRICT'), nullable=False)
    code = db.Column(db.String(15), nullable=False)
    type = db.Column(db.String(60), nullable=False)
    life_in_sec = db.Column(db.Integer,nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    expired_at = db.Column(db.DateTime, nullable=True)

    used_at = db.Column(db.DateTime, nullable=True)


    # Relationships
    __table_args__ = (db.UniqueConstraint('user_id', 'code', name='_user_verifcation_code_uc'),)

    def to_dict(self):
            return {
                "code": self.code,
                "usedr_id":self.user_id,
                'expired_at':self.expired_at,
                'type':self.type 

            }    

