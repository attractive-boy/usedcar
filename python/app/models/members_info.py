from app import db

class Member(db.Model):
    __tablename__ = 'members_info'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    phone_number = db.Column(db.String(15), unique=True, nullable=False)
    license_plate = db.Column(db.String(10), nullable=False)
    discount = db.Column(db.Numeric(3, 1), nullable=False)
    membership_type = db.Column(db.String(10), nullable=False)
    activation_amount = db.Column(db.Numeric(10, 2), nullable=False)
    validity_period = db.Column(db.Date, nullable=False)
    notes = db.Column(db.String(255))

    repair_records = db.relationship('RepairRecord', backref='member', lazy=True)
