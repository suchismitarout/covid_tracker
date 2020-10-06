from app.model.state_dist_stats import StateDistCovidStats
from app import db


class StateDistStatsDao():
    def create_one(self, record):
        db.session.StateDistCovidStats.add(**record)
        db.session.commit()

    def create_many(self, records):
        pass

    def find_one(self, params):
        try:
            res = StateDistCovidStats.query.filter_by(**params).first()
            return res
        except Exception as e:
            print("Exception occured during querying DB...", e.args, e)
            return {"Status": "Falied", "Msg": "Requested info not found in DB"}

    def delete_one(self, record):
        pass

    def update(self, record):
        pass
