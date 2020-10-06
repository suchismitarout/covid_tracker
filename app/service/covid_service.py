import requests
from app.model.state_dist_stats import StateDistCovidStats
from app.model.state_stats import StateCovidStats
from app import db
import logging
from app.utils.common import object_to_dict
from app.dao.state_stats_dao import StateStatsDao
from app.dao.state_dist_stats_dao import StateDistStatsDao
from app.apis.state_dist_apis import SateDistApi


class CovidService():

    def __init__(self):
        self.state_stats_dao = StateStatsDao()
        self.state_dist_stats_dao = StateDistStatsDao()
        self.state_dist_apis = SateDistApi()

    def get_all_covid_info(self):
        return self.state_dist_apis.get_records()

    def get_covid_result_state_dist_wise(self, state, district):
        if state and district:
            records = self.state_dist_apis.get_records()
            print("all records received from api", records)
            print("received response types..".format(type(records)))
            record = {}
            record['State'] = state
            record['District'] = district
            record['Date'] = '24/09/2020'
            for k, v in records.items():
                if k == state:
                    print("record found...")
                    print("record", v)
                    for a, b in v['districtData'].items():
                        if a == district:
                            print("district record found")
                            print("district got", b)
                            record['Active'] = b['active']
                            record['Confirmed'] = b['confirmed']
                            record['Deceased'] = b['deceased']
                            record['Recovered'] = b['recovered']
            print(record)
            return record
        elif state:

            records = self.state_dist_apis.get_records()
            print("all records received from ext api", records)

            del records['State Unassigned']
            new_record = {}
            new_record['State'] = state
            new_record['Active'] = 0
            new_record['Confirmed'] = 0
            new_record['Deceased'] = 0
            new_record['Recovered'] = 0
            new_record['District'] = 0
            new_record['Date'] = '24/09/2020'

            for k, v in records.items():
                if k == state:
                    for k, v in v['districtData'].items():
                        if k not in ('State Pool', 'Others'):
                            new_record['District'] = new_record['District'] + 1
                            new_record['Active'] = new_record['Active'] + v['active']
                            new_record['Confirmed'] = new_record['Confirmed'] + v['confirmed']
                            new_record['Deceased'] = new_record['Deceased'] + v['deceased']
                            new_record['Recovered'] = new_record['Recovered'] + v['recovered']
            print("Returning response from the api..", new_record)
            return new_record

    def get_covid_info_dist_wise_and_update(self, state, dist):
        print("ENTRY.. get_covid_info_dist_wise_and_update")
        try:
            resp = self.state_dist_stats_dao.find_one({"State": state, "District": dist})
            print("Data already present in the DB", resp)

            if resp is None:
                print("data is already not present in db, lets query the api")
                resp = self.get_covid_result_state_dist_wise(state, dist)

                self.state_dist_stats_dao.create_one(**resp)


        except Exception:
            print("exception occured...")
            logging.info("Got response.. {}".format(resp))
        print("Returning response..{}".format(resp))
        return resp

    def get_covid_status_state_wise_and_update(self, state):
        logging.info("To check & update in state_stats table")
        try:
            resp = self.state_stats_dao.find_one({"State": state})
            print("response we got from StateCovidStats db", resp)

            if resp is None:
                print("data is not present in db ,so query from ext api")
                resp = self.get_covid_result_state_dist_wise(state, None)

                # call method to update the values now in the table
                self.state_stats_dao.update(resp)
                print("Returning.... with res", resp)
        except Exception as e:
            print("exception occured", e.args, e)
            return {"status": "Failed", "Msg": "couldn't update the db"}
        print("Returning final resp..", resp)
        print(object_to_dict(resp))
        print("====================")
        return object_to_dict(resp)
