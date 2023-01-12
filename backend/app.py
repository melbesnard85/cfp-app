import os
from flask import Flask, request, jsonify
from flask_bcrypt import Bcrypt
from itsdangerous import (TimedJSONWebSignatureSerializer as Serializer, SignatureExpired, BadSignature)

from flask_jwt_extended import JWTManager
from flask_restful import Api

from errors import errors
from config import BaseConfig
from models.db import initialize_db
from routes.api import initialize_routes
from models.User import User

from flask_cors import CORS

app = Flask(__name__, static_folder="./frontend/build")
app.config["JWT_SECRET_KEY"] = "super-secret"
api = Api(app, errors=errors)
# Database connection
try:
	app.config.from_object(BaseConfig)
	initialize_db(app)
except Exception as e:
	print(e)

# Salt user password
bcrypt = Bcrypt(app)
# JWT instances
jwt = JWTManager(app)
# CORS enabled
CORS(app)

# Get roles for authenticated user
@jwt.additional_claims_loader
def add_claims_to_access_token(user):
    return {'roles': user.roles}

# Load user identity
@jwt.user_identity_loader
def user_identity_lookup(user):
    return user.email

# API (Routing) Configuration Initialization
initialize_routes(api)

# Admin account initialization for first uses
user = User.objects(email='admin@gmail.com')
if not user:
    login = User(email='admin@gmail.com', password='asdfASDF', roles=['admin'])
    login.hash_password()
    login.save()

if __name__ == "__main__":
	port = int(os.environ.get('PORT', 5000))
	app.run(host='localhost', port=port)