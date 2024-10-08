#!/usr/bin/env python3
"""
Route module for the API
"""
from os import getenv
from api.v1.views import app_views
from flask import Flask, jsonify, abort, request
from flask_cors import (CORS, cross_origin)
import os


app = Flask(__name__)
app.register_blueprint(app_views)
CORS(app, resources={r"/api/v1/*": {"origins": "*"}})

auth_type = os.getenv("AUTH_TYPE")
if auth_type == "basic_auth":
    from api.v1.auth.basic_auth import BasicAuth
    auth = BasicAuth()
elif auth_type == "session_auth":
    from api.v1.auth.session_auth import SessionAuth
    auth = SessionAuth()


@app.errorhandler(404)
def not_found(error) -> str:
    """ Not found handler
    """
    return jsonify({"error": "Not found"}), 404


@app.errorhandler(401)
def not_authorized(error) -> str:
    """ Not authorized
    """
    return jsonify({"error": "Unauthorized"}), 401


@app.errorhandler(403)
def forbidden(error) -> str:
    """ Forbidden
    """
    return jsonify({"error": "Forbidden"}), 403


@app.before_request
def authenticate():
    """
    Authentication
    """
    if auth:
        excluded = ['/api/v1/status/',
                    '/api/v1/unauthorized/',
                    '/api/v1/forbidden/',
                    '/api/v1/auth_session/login/']
        require_auth = auth.require_auth(request.path, excluded)
        if require_auth:
            if not auth.authorization_header(request) and\
                    auth.session_cookie(request) is None:
                abort(401)
            user = auth.current_user(request)
            if not auth.session_cookie:
                return None
            if user is None:
                abort(403)
            request.current_user = user


if __name__ == "__main__":
    host = getenv("API_HOST", "0.0.0.0")
    port = getenv("API_PORT", "5000")
    app.run(host=host, port=port)
