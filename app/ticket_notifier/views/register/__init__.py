from flask import Blueprint
from .register_view import RegisterView

# This instance of a Blueprint that represents the sales_data blueprint
register_bp = Blueprint('register', __name__, url_prefix="/")

# Define the rule for the registration url --->  /register_view
register_view = RegisterView.as_view('register_view')
# Then add the rule to the blueprint
register_bp.add_url_rule(
    '/register',
    view_func=register_view,
    methods=['POST'])

register_bp.add_url_rule(
    '/register/<string:contact>',
    view_func=register_view,
    methods=['GET', 'DELETE'])
