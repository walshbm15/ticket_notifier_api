from flask import current_app, make_response, jsonify, abort


def server_error(error):
    # log error
    current_app.logger.error(error)

    # Create a response containing an string error message
    response = {
        'message': "Internal Server Error"
    }
    # Return a server error using the HTTP Error Code 500 (Internal Server Error)
    abort(make_response(jsonify(response), 500))
