from flask import Flask, _app_ctx_stack
from flask_login import LoginManager
from sqlalchemy.orm import scoped_session

from database import SessionLocal, engine
from models.User import User
from routes.controller_blueprints import route_blueprints, routes_auth
from setup import provision_database, populate_tables

app = Flask(__name__)
app.session = scoped_session(SessionLocal, scopefunc=_app_ctx_stack.__ident_func__)

app.config['SECRET_KEY'] = "Form Secret Key"
provision_database(engine)
populate_tables(app.session)

##### Login #####
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'routes.login'


@login_manager.user_loader
def load_user(user_id):
    try:
        return User.get_user(app.session, user_id)
    except:
        return None


app.register_blueprint(route_blueprints)
app.register_blueprint(routes_auth)

if __name__ == '__main__':
    app.run(debug=True)
