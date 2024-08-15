#!/usr/bin/env python3
"""API Routes for Authentication Service"""
from auth import Auth
from flask import (
    Flask,
    jsonify,
    make_response,
    request,
    abort,
    redirect
)


app = Flask(__name__)
AUTH = Auth()


@app.route('/', methods=['GET'], strict_slashes=False)
def hello():
    """root
    """
    return jsonify({"message": "Bienvenue"})


@app.route('/users', methods=['POST'], strict_slashes=False)
def create_user():
    '''
    creating user using Auth module
    '''
    email = request.form.get('email', None)
    password = request.form.get('password', None)
    try:
        AUTH.register_user(email, password)
    except ValueError:
        return make_response(jsonify(
            {"message": "email already registered"}), 400)
    return make_response(jsonify(
        {"email": F"{email}", "message": "user created"}), 200)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
