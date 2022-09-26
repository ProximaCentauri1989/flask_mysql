"""
    api/users
"""

from flask_cors import CORS
from flask import request
from apiflask import APIBlueprint
from .utils import abort
from ..models import User, Payment
from ..db import get_connection
from ..api_models.api_models import UserIn, UserOut, APIResponseBaseReduced, APIResponseGetUsers

session = get_connection()
blueprint = APIBlueprint('users', __name__)

@blueprint.route('/users', methods=['GET'])
@blueprint.output(APIResponseGetUsers)
def getAll():
    try:
        users = []
        show_payments = request.args.get('show_payments', None)
        if show_payments:
            users = session.query(User).join(Payment, isouter=True).all() # isouter=True will include users which do not have payments
        else:
            users = session.query(User).all() # autojoin works here which is unexpected
        return  { 'data': [item.as_json for item in users] }
    except Exception as err:
        print(err)
        abort(500, description='Failed to get users')

@blueprint.route('/user/<int:id>', methods=['GET'])
@blueprint.output(UserOut)
def getById(id):
    try:
        user = session.get(User, id)
        if user is not None:
            return user.as_json
        else:
            abort(404, "Not found")
    except Exception as err:
        print(err)
        abort(500, description='Failed to get users')

@blueprint.route('/user/<int:id>', methods=['DELETE'])
@blueprint.output(APIResponseBaseReduced)
def deleteById(id):
    try:
        user = session.get(User, id)
        if not user:
            abort(404, description="No user exist by id {}".format(id))
        
        session.delete(user)
        session.commit()
        return { "result": "success" }
    except Exception as err:
        abort(500, description='Failed to delete user')

@blueprint.route('/user', methods=['POST'])
@blueprint.input(UserIn)
@blueprint.output(APIResponseBaseReduced)
def post(data):
    """Create new user
        Returns:
            200: txid
            500: error message
        """
        
    try:
        username = data.get('username')
        email = data.get('email')
        password = data.get('password')

        session.add(User(
            username=username,
            email=email,
            password_hash=password
        ))
        session.commit()
        return { "result": "success" }
    except Exception as err:
        print(err)
        abort(500, description='Failed to create new user')


CORS(blueprint)
