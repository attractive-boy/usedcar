from datetime import datetime
from app import db

def safe_float(value):
    try:
        return float(value)
    except (TypeError, ValueError):
        return 0

class VehicleInfo(db.Model):
    __tablename__ = 'vehicle_info'

    id = db.Column(db.Integer, primary_key=True)
    photo = db.Column(db.String(255))  # 存储照片的路径或URL
    model = db.Column(db.String(50), nullable=False)
    year = db.Column(db.String(7), nullable=False)
    mileage = db.Column(db.Integer, nullable=False)
    license_plate = db.Column(db.String(20), nullable=False)
    account_number = db.Column(db.String(50), nullable=False)
    color = db.Column(db.String(20), nullable=False)
    insurance_compulsory = db.Column(db.Boolean, default=False)
    insurance_compulsory_end_date = db.Column(db.Date)
    insurance_third_party = db.Column(db.Boolean, default=False)
    insurance_third_party_end_date = db.Column(db.Date)
    previous_owner_name = db.Column(db.String(50))
    previous_owner_wechat = db.Column(db.String(50))
    previous_owner_phone = db.Column(db.String(20))
    vehicle_frame_number = db.Column(db.String(50), nullable=False)
    purchase_amount = db.Column(db.Float, nullable=False)
    # purchaser = db.Column(db.String(50), nullable=False) 采用员工User 表关联
    purchaser_id = db.Column(db.Integer, db.ForeignKey('user_info.id'), nullable=False)
    additional_fee = db.Column(db.Boolean, default=False)
    additional_fee_detail = db.Column(db.String(255))
    additional_fee_amount = db.Column(db.Float)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    

    def __init__(self, json):
        self.photo = json.get('photo')
        self.model = json.get('model')
        self.year = json.get('year')
        self.mileage = json.get('mileage')
        self.license_plate = json.get('licensePlate')
        self.account_number = json.get('accountNumber')[0]
        self.color = json.get('color')
        
        # 将字符串'true'/'false'转换为布尔值
        self.insurance_compulsory = json.get('insuranceCompulsory', 'false').lower() == 'true'

        insurance_compulsory_end_date_str = json.get('insuranceCompulsoryEndDate', '')
        self.insurance_compulsory_end_date = (
            datetime.strptime(insurance_compulsory_end_date_str, '%Y-%m-%d').date()
            if insurance_compulsory_end_date_str else None
        )
        
        insurance_third_party_end_date_str = json.get('insuranceThirdPartyEndDate', '')
        self.insurance_third_party_end_date = (
            datetime.strptime(insurance_third_party_end_date_str, '%Y-%m-%d').date()
            if insurance_third_party_end_date_str else None
        )
        
        self.insurance_third_party = json.get('insuranceThirdParty', 'false').lower() == 'true'

        insurance_third_party_end_date_str = json.get('insuranceThirdPartyEndDate', '')
        self.insurance_third_party_end_date = (
            datetime.strptime(insurance_third_party_end_date_str, '%Y-%m-%d').date()
            if insurance_third_party_end_date_str else None
        )
        
        self.previous_owner_name = json.get('previousOwnerName')
        self.previous_owner_wechat = json.get('previousOwnerWeChat')
        self.previous_owner_phone = json.get('previousOwnerPhone')
        self.vehicle_frame_number = json.get('vehicleFrameNumber')
        self.purchase_amount = safe_float(json.get('purchaseAmount', 0))
        
        # 注意：原代码中有两处设置了self.purchaser，其中一处应该是设置purchaser_id
        self.purchaser_id = json.get('purchaser')[0]  # 假设json中的'purchaser'是用户ID而不是用户名
        self.additional_fee = json.get('additionalFee', 'false').lower() == 'true'
        self.additional_fee_detail = json.get('additionalFeeDetail')
        # self.additional_fee_amount = json.get('additionalFeeAmount')
        # 尝试转换成浮点 类型 转换不了就给空
        self.additional_fee_amount = safe_float(json.get('additionalFeeAmount', None))

    def to_dict(self):
        return {
            'id': self.id,
            'photo': self.photo,
            'model': self.model,
            'year': self.year,
            'mileage': self.mileage,
            'license_plate': self.license_plate,
            'account_number': self.account_number,
            'color': self.color,
            'insurance_compulsory': self.insurance_compulsory,
            'insurance_compulsory_end_date': self.insurance_compulsory_end_date,
            'insurance_third_party': self.insurance_third_party,
            'insurance_third_party_end_date': self.insurance_third_party_end_date,
            'previous_owner_name': self.previous_owner_name,
            'previous_owner_wechat': self.previous_owner_wechat,
            'previous_owner_phone': self.previous_owner_phone,
            'vehicle_frame_number': self.vehicle_frame_number,
            'purchase_amount': self.purchase_amount,
            'purchaser': self.purchaser_id,
            'additional_fee': self.additional_fee,
            'additional_fee_detail': self.additional_fee_detail,
            'additional_fee_amount': self.additional_fee_amount,
            'created_at': self.created_at,
        }
    #更新或者创建
    def save(self):
        db.session.add(self)
        #
        db.session.commit()

    