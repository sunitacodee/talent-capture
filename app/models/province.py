from app.extensions import db

class Province(db.Model):
    __tablename__ = 'provinces'
    
    id = db.Column(db.Integer, primary_key=True)  # 1 to 7
    name_en = db.Column(db.String(100), nullable=False, unique=True)
    name_np = db.Column(db.String(100), nullable=False, unique=True)
    
    # Relationships
    districts = db.relationship('District', backref='province', lazy=True, cascade="all, delete-orphan")

    def __repr__(self):
        return f"<Province {self.name_en}>"
    
    def to_dict(self):
        return {
            "id": self.id,
            "name":self.name_en
        }


