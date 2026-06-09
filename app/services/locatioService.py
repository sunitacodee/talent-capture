from datetime import datetime
from app.extensions import db
from app.models.province import Province
from app.models.district import District
from app.models.localBodyWard import LocalBodyWard
from app.models.localbody import LocalBody
from app.models.user import User
from app.validations.employeeValidator import validate_employee
from flask import current_app

class LocationService:
    @staticmethod
    def getAllProvinces()->list[dict]:
        try:       
            provinces = Province.query.order_by(Province.name_en).all()
            return [p.to_dict() for p in provinces]
        except Exception as e:
            current_app.logger.exception(f'error fetching provinces: {e}')
            raise RuntimeError("unable to retrieve province data.")
    
    
    @staticmethod
    def getAllDistrictsByProvince(provinceId: int)->list[dict]:
        try:       
           
            districts = District.query.filter_by(province_id=provinceId)\
                              .order_by(District.name_en)\
                              .all()
            return [d.to_dict() for d in districts]
        except Exception as e:
            # current_app.logger.exception(f'error fetching districts: {e}')
            raise RuntimeError("unable to retrieve district data.")
    
    @staticmethod
    def getAllLocalbodiesByDistrict(districtId: int)->list[dict]:
        try:       
            districts = LocalBody.query.filter_by(district_id=districtId).order_by(LocalBody.name_en).all()
            return [lb.to_dict() for lb in districts]
        except Exception as e:
            current_app.logger.exception(f'error fetching locabodies: {e}')
            raise RuntimeError("unable to retrieve localbody data.")
    
    @staticmethod
    def getAllWardsByLocalbody(localbodyId: int)->list[dict]:
        try:       
            districts = LocalBodyWard.query.filter_by(local_body_id=localbodyId)\
                .order_by(LocalBodyWard.ward_number)\
                    .all()
            return [lb.to_dict() for lb in districts]
        except Exception as e:
            current_app.logger.exception(f'error fetching wards: {e}')
            raise RuntimeError("unable to retrieve ward data.")
    
    