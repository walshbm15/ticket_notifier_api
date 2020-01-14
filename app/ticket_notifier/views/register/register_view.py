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
            email = post_data.get("email", "")
            mobile = post_data.get("mobile", "")
            user = User.get_user(email)
            # User email didn't exist check using mobile
            if not user:
                user = User.get_user(mobile)

            if not user:
                # There is no user so we'll try to register them
                # Register the user
                user = User(name=post_data.get("name", ""),
                            email=email,
                            mobile=mobile)
                user.save()

                response = {
                    'message': 'You registered successfully.'
                }
                # Return a response notifying the user that they registered successfully
                return make_response(jsonify(response)), 201

            else:

                user = User(name=post_data.get("name", ""),
                            email=post_data.get("email", user.email),
                            mobile=post_data.get("mobile", user.mobile))
                user.save()
                # User information updated
                response = {
                    'message': 'User information updated.'
                }

                return make_response(jsonify(response)), 202
        except Exception as e:
            server_error(e)

    def get(self, contact=""):
        """Handle GET request for this view. Url ---> /register"""

        try:
            user = User.get_user(contact)
            response = user.get_user_dict()

            return make_response(jsonify(response)), 200
        except HTTPException:
            raise
        except Exception as e:
            server_error(e)

    def delete(self, contact=""):
        """Handle DELETE request for this view. Url ---> /register"""

        try:
            user = User.get_user(contact)
            user.delete()
            response = "User information has been deleted"

            return make_response(jsonify(response)), 200
        except HTTPException:
            raise
        except Exception as e:
            server_error(e)
