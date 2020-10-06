from app import app
from app.routes.state_covid_tracker_routes import covid_var


if __name__ == '__main__':
    app.register_blueprint(covid_var)
    app.run()