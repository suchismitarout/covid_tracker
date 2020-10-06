from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import configparser

config = configparser.ConfigParser()
config.read('C:/Users/Suchismita/PycharmProjects/covid_tracker/app/resources/config.ini')
config.sections()
user = config['mysql']['user']
pwd = config['mysql']['pwd']
host = config['mysql']['host']
db = config['mysql']['db']

app = Flask(__name__)

app.config['SECRET_KEY'] = 'my_sec_key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://{user}:{pwd}''@{host}/{db}'.format(user=user, pwd=pwd,
                                                                                            host=host, db=db)

# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:''ninky@localhost/user_profile'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
