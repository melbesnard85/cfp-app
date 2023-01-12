# from mongoengine import *

# class User(Document):
# 	email		= StringField(max_length=255, unique=True)
# 	password	= StringField(max_length=255, required=True)
# 	role		= StringField(max_length=255, required=True)


# Import from system libraries
from flask_bcrypt import generate_password_hash, check_password_hash

# Import from application modules
from models.db import db

# Object Document Model (ODM) for User Objects
class User(db.Document):
    email = db.EmailField(required=True, unique=True)
    password = db.StringField(required=True)
    roles = db.ListField(db.StringField(), default=['default'])

    # function to hash a password for security encryption
    def hash_password(self):
        self.password = generate_password_hash(self.password).decode('utf8')

    # function to hash a password for security decryption
    def check_password_hash(self, password):
        return check_password_hash(self.password, password)
