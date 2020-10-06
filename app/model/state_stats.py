from app import db


class StateCovidStats(db.Model):
    __tablename__ = 'statecovidstats'
    id = db.Column(db.Integer, primary_key=True)
    State = db.Column(db.String(20))
    District = db.Column(db.String(20))
    Active = db.Column(db.Integer)
    Confirmed = db.Column(db.Integer)
    Deceased = db.Column(db.Integer)
    Recovered = db.Column(db.Integer)
    Date = db.Column(db.String(10))

    def __init__(self, State, Active, District, Confirmed, Deceased, Recovered, Date):
        self.State = State
        self.Active = Active
        self.District = District
        self.Confirmed = Confirmed
        self.Deceased = Deceased
        self.Recovered = Recovered
        self.Date = Date

    def __repr__(self):
        # return {"State": self.State, "District": self.District, "Active": self.Active, "Confirmed": self
        #     .Confirmed, "Deceased": self.Deceased, "Recovered": self.Recovered, "Date": self.Date}
        return '{State: ' + self.State + ', Active: ' + str(self.Active) + ', Confirmed: ' + str(
            self.Confirmed) + ', Deceased: ' + str(self.Deceased) + ',Recovered: ' + str(
            self.Recovered) + ', Date: ' + self.Date + '}'
