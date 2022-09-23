"""
    api/users
"""

from flask_expects_json import expects_json
from flask_cors import CORS
from flask import Blueprint, request
from .schemas.schemas import user_schema
from ..models import User
from ..db import get_connection

session = get_connection()
blueprint = Blueprint('users', __name__)

def format_response(code, reason=None, data=None):
    resp = {
        "result": "Success" if (code == 200) else "Failed"
    }
    if reason:
        resp["reason"] = reason
    if data:
        resp["data"] = data

    return resp, code

@blueprint.route('/users', methods=['GET'])
def getAll():
    try:
        users = session.query(User).all()
        return format_response(200, data=[item.as_json for item in users])
    except Exception as err:
        print(err)
        return format_response(500, reason='Failed to get users')

@blueprint.route('/user/<int:id>', methods=['GET']) 
def getById(id):
    try:
        user = session.get(User, id)
        if user is not None:
            return format_response(200, data=user.as_json)
        else:
            return format_response(404, "Not found")
    except Exception as err:
        print(err)
        return format_response(200, reason='Failed to get users')

@blueprint.route('/user/<int:id>', methods=['DELETE']) 
def deleteById(id):
    try:
        user = session.get(User, id)
        if user is None:
            return format_response(404, "Not found")
        
        session.delete(user)
        session.commit()
        return format_response(200)
    except Exception as err:
        print(err)
        return format_response(500, reason='Failed to delete user')

@blueprint.route('/user', methods=['POST']) 
@expects_json(user_schema)
def post():
    """Create new user
        Returns:
            200: txid
            500: error message
        """
        
    try:
        username = request.json.get('username')
        email = request.json.get('email')
        password = request.json.get('password')

        session.add(User(
            username=username,
            email=email,
            password_hash=password
        ))
        session.commit()  
        return format_response(200)
    except Exception as err:
        print(err)
        return format_response(500, reason='Failed to create new user')


CORS(blueprint)
