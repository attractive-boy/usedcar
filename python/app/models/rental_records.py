from app import db

class RentalRecord(db.Model):
    __tablename__ = 'rental_records'
    id = db.Column(db.Integer, primary_key=True)
    car_model = db.Column(db.String(50), nullable=False)
    rental_stock = db.Column(db.Integer, nullable=False)
    booking_time = db.Column(db.DateTime, nullable=False)
    current_time = db.Column(db.DateTime, nullable=False)
    renter_name = db.Column(db.String(50), nullable=False)
    renter_phone = db.Column(db.String(15), nullable=False)
    license_photo = db.Column(db.LargeBinary)
    contract_photo = db.Column(db.LargeBinary)
    member_discount = db.Column(db.Numeric(3, 1))
    rental_amount = db.Column(db.Numeric(10, 2), nullable=False)
    order_date = db.Column(db.Date, nullable=False)
