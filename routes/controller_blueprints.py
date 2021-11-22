from flask import Blueprint
from flask_login import login_required

from controllers.auth_controller import logout,login
from controllers.dashboard_controller import dashboard
from controllers.home_controller import home
from controllers.profile_controller import profile

route_blueprints = Blueprint('routes', __name__, template_folder='templates')
routes_auth = Blueprint('routes_auth', __name__, template_folder='templates')


@routes_auth.before_request
@login_required
def before_request():
    """ Protect all of the admin endpoints. """
    pass


route_blueprints.route('/', methods=['GET'])(home)
route_blueprints.route('/login', methods=['GET', 'POST'])(login)
routes_auth.route('/dashboard', methods=['GET', 'POST'])(dashboard)
routes_auth.route('/logout', methods=['GET', 'POST'])(logout)
routes_auth.route('/profile', methods=['GET'])(profile)


