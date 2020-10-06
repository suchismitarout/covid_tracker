from flask import request, jsonify, Blueprint, json
from app.service.covid_service import CovidService

covid_var = Blueprint('covid', __name__)

##########################
#  Creating Objects      #
##########################
covid_service = CovidService()


@covid_var.route('/getall', methods=['GET'])
def get_all_covid_info_state_district_wise():
    return covid_service.get_all_covid_info()


@covid_var.route('/get_state_dist_wise', methods=['GET'])
def get_covid_info_state_district_wise():
    record = request.args.to_dict()
    print("record got", record)
    if record['State'] and record.get('districtData', None):
        print("inside if got state from endpoint", record['State'])
        print("check district from endpoint", record['districtData'])
        state = record['State']
        district = record['districtData']
        return covid_service.get_covid_info_dist_wise_and_update(state, district)
    elif record['State']:
        print("inside elif got state from endpoint", record['State'])
        state = record['State']
        return covid_service.get_covid_status_state_wise_and_update(state)
