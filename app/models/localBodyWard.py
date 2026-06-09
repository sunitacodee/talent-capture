from app.extensions import db

class LocalBodyWard(db.Model):
    __tablename__ = 'local_body_wards'
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    local_body_id = db.Column(db.Integer, db.ForeignKey('local_bodies.id', ondelete='CASCADE'), nullable=False)
    ward_number = db.Column(db.Integer, nullable=False)
    
    __table_args__ = (
        db.UniqueConstraint('local_body_id', 'ward_number', name='_local_body_ward_uc'),
        db.CheckConstraint('ward_number > 0 AND ward_number <= 40', name='valid_ward_range')
    )

    def __repr__(self):
        return f"<Ward {self.ward_number} of LocalBody ID {self.local_body_id}>"
    
    def to_dict(self):
        return {
            "id": self.id,
            "name":self.ward_number,
        }