from flask import Response, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt, get_jwt_identity, create_access_token
from flask_jwt_extended.exceptions import NoAuthorizationError
from flask_restful import Resource
from mongoengine import FieldDoesNotExist, NotUniqueError, DoesNotExist, InvalidQueryError

from errors import NoAuthorizationError, InternalServerError, SchemaValidationError, EmailAlreadyExistsError, \
    DeletingUserError, UpdatingUserError
from models.User import User


class AdminApi(Resource):
    @jwt_required
    def get(self):
        print('roles : ', str(get_jwt()['roles']))
        try:
            if 'admin' in get_jwt()['roles']:
                users = User.objects().to_json()
                return Response(users, mimetype='application/json', status=200)
        except NoAuthorizationError:
            raise NoAuthorizationError
        except Exception:
            raise InternalServerError

    @jwt_required
    def post(self):
        try:
            if 'admin' in get_jwt()['roles']:
                body = request.get_json()
                user = User(**body)
                user.hash_password()
                user.save()
                id = user.id
                return {'id': str(id)}, 201
        except FieldDoesNotExist:
            raise SchemaValidationError
        except NotUniqueError:
            raise EmailAlreadyExistsError
        except Exception:
            raise InternalServerError