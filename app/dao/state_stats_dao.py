from app import db
from app.model.state_stats import StateCovidStats


class StateStatsDao():
    def create_one(self, record):
        pass

    def create_many(self, records):
        pass

    def find_one(self, params):
        try:
            res = StateCovidStats.query.filter_by(**params).first()
            return res
        except Exception as e:
            print("Exception occured during querying DB...", e.args, e)
            return {"Status": "Falied", "Msg": "Requested info not found in DB"}

    def delete(self):
        pass

    def update(self, data):
        statestats = StateCovidStats(**data)
        db.session.add(statestats)
        db.session.commit()
