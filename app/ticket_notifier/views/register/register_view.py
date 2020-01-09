from flask.views import MethodView
from flask import make_response, request, jsonify, g
from flask.views import MethodView
from flask import make_response, request, jsonify
from app.ticket_notifier.models.user import User
from app.ticket_notifier.utils.helper import server_error
from werkzeug.exceptions import HTTPException
import json


class RegisterView(MethodView):
    """This class registers a new user."""

    def post(self):
        """Handle POST request for this view. Url ---> /register"""

        post_data = json.loads(request.get_json().get("body"))

        try:
            # Query to see if the user already exists
            user = User.query.filter_by(username=post_data['username']).first()

            if not user:
                # There is no user so we'll try to register them
                # Register the user
                user = User(name=post_data.get("name"),
                            email=post_data("email"),
                            mobile=post_data.get("mobile"))
                user.save()

                response = {
                    'message': 'You registered successfully. Please log in.'
                }
                # return a response notifying the user that they registered successfully
                return make_response(jsonify(response)), 201

            else:
                # There is an existing user. We don't want to register users twice
                # Return a message to the user telling them that they they already exist
                response = {
                    'message': 'User already exists. Please login.'
                }

                return make_response(jsonify(response)), 202
        except Exception as e:
            server_error(e)

    def get(self, contact=None):
        """Handle GET request for this view. Url ---> /register"""

        try:
            response = User.get_user(contact)

            return make_response(jsonify(response)), 200
        except HTTPException:
            raise
        except Exception as e:
            server_error(e)
