import os
from flask import Blueprint, Flask, request, jsonify
import datetime

import flask
from app.models.vehicle_info import VehicleInfo
from config import Config

bp = Blueprint('vehicle', __name__)


#收车录入提交
@bp.route('', methods=['POST'])
def vehicle_route():
    try:
        data = request.get_json()
        
        vehicle_info = VehicleInfo(data)
        VehicleInfo.save(vehicle_info)
        return jsonify({'message': 'Vehicle info saved successfully'}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    
#照片上传
@bp.route('/upload', methods=['POST'])
def upload_photo():
    try:
        file = request.files['file']
        if file:
            filename = file.filename
            file.save(os.path.join(Config.UPLOAD_FOLDER, filename))
            return jsonify({'message': 'File uploaded successfully', 'filename': filename}), 200
        else:
            return jsonify({'error': 'No file part'}), 400
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    
#图片下载api
@bp.route('/download/<filename>', methods=['GET'])
def download_photo(filename):
    try:
        if filename:
            return flask.send_file(os.path.join(Config.UPLOAD_FOLDER , filename), as_attachment=True)
        else:
            return jsonify({'error': 'No filename provided'}), 400
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    
#获取车辆列表
@bp.route('', methods=['GET'])
def get_vehicle_list():
    try:
        vehicles = VehicleInfo.query.all()
        return jsonify([vehicle.to_dict() for vehicle in vehicles]), 200
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    
    
    


