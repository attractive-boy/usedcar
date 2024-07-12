from app import db

class RepairRecord(db.Model):
    __tablename__ = 'repair_records'
    id = db.Column(db.Integer, primary_key=True)
    member_id = db.Column(db.Integer, db.ForeignKey('members.id'), nullable=False)
    discount = db.Column(db.Numeric(3, 1), nullable=False)
    pre_sale = db.Column(db.Boolean, nullable=False)
    post_sale = db.Column(db.Boolean, nullable=False)
    car_model = db.Column(db.String(50), nullable=False)
    car_year = db.Column(db.Date, nullable=False)
    car_photo = db.Column(db.LargeBinary)
    repair_type = db.Column(db.String(50), nullable=False)
    part_name = db.Column(db.String(50))
    in_store_repair = db.Column(db.Boolean, nullable=False)
    third_party_repair = db.Column(db.String(50))
    tools_used = db.Column(db.String(50), nullable=False)
    cost = db.Column(db.Numeric(10, 2), nullable=False)
    record_date = db.Column(db.Date, nullable=False)
