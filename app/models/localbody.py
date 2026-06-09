from app.extensions import db

class LocalBody(db.Model):
    __tablename__ = 'local_bodies'
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    district_id = db.Column(db.Integer, db.ForeignKey('districts.id', ondelete='RESTRICT'), nullable=False)
    name_en = db.Column(db.String(150), nullable=False)
    name_np = db.Column(db.String(150), nullable=False)
    body_type = db.Column(db.String(50), nullable=False)  # 'Metropolitan', 'Sub-Metropolitan', 'Municipality', 'Rural Municipality'
    
    # Relationships
    wards = db.relationship('LocalBodyWard', backref='local_body', lazy=True, cascade="all, delete-orphan")
    
    __table_args__ = (db.UniqueConstraint('district_id', 'name_en', 'body_type', name='_district_local_body_uc'),)

    def __repr__(self):
        return f"<LocalBody {self.name_en} ({self.body_type})>"

    def to_dict(self):
            return {
                "id": self.id,
                "name":self.name_en
            }