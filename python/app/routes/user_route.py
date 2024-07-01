from flask import Blueprint, Flask, request, jsonify
import datetime
from app.models.user_info import UserInfo
from config import Config

bp = Blueprint('user', __name__)

#查找所有用户
@bp.route('', methods=['GET'])
def getUsers():
    try:
        users = UserInfo.query.all()
        user_list = [user.to_dict() for user in users]
        return jsonify({'status': 'success', 'data': user_list}), 200
    except Exception as e:
        return jsonify({'status': 'error', 'message': 'Failed to fetch users'}), 500