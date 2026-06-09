from flask import Blueprint, request, jsonify
from app.services.locatioService import LocationService

location_bp = Blueprint("locations", __name__)


@location_bp.route('/provinces')
def getAllProvinces():
    try:
        provinces = LocationService.getAllProvinces()
        return jsonify({"success": True, "data": provinces}), 200
    except Exception as e:
        return jsonify({
            "success": False, 
            "message": str(e)  
        }), 500
    
@location_bp.route("/provinces/<int:provinceId>/districts")
def getAllDistrictsByProvince(provinceId):
    try:
        districts = LocationService.getAllDistrictsByProvince(provinceId)
        return jsonify({"success": True, "data": districts}), 200
    except Exception as e:
        return jsonify({
            "success": False, 
            "message": str(e)  
        }), 500


@location_bp.route("/districts/<int:districtId>/localbodies")
def getAllLocalbodiesByDistrict(districtId):
    try:
        localbodies = LocationService.getAllLocalbodiesByDistrict(districtId)
        return jsonify({"success": True, "data": localbodies}), 200
    except Exception as e:
        return jsonify({
            "success": False, 
            "message": str(e)  
        }), 500

@location_bp.route("/localbodies/<int:localbodyId>/wards")
def getAllWardsByLocalbody(localbodyId):
    try:
        wards = LocationService.getAllWardsByLocalbody(localbodyId)
        return jsonify({"success": True, "data": wards}), 200
    except Exception as e:
        return jsonify({
            "success": False, 
            "message": str(e)  
        }), 500

