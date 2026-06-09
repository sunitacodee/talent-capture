from app.extensions import db
class District(db.Model):
    __tablename__ = 'districts'
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    province_id = db.Column(db.Integer, db.ForeignKey('provinces.id', ondelete='RESTRICT'), nullable=False)
    name_en = db.Column(db.String(100), nullable=False)
    name_np = db.Column(db.String(100), nullable=False)
    
    # Relationships
    local_bodies = db.relationship('LocalBody', backref='district', lazy=True, cascade="all, delete-orphan")
    
    __table_args__ = (db.UniqueConstraint('province_id', 'name_en', name='_province_district_uc'),)

    def __repr__(self):
        return f"<District {self.name_en}>"
    
    def to_dict(self):
            return {
                "id": self.id,
                "name":self.name_en    
            }    

