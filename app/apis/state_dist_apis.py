import requests


class SateDistApi():

    def get_records(self):
        response = requests.get("https://api.covid19india.org/state_district_wise.json")
        records = response.json()
        return records
