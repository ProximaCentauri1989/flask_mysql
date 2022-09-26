"""
    api/payments
"""

from flask_expects_json import expects_json
from flask_cors import CORS
from flask import Blueprint, request
from .schemas.schemas import payment_schema
from .utils import abort
from ..models import Payment
from ..db import get_connection

session = get_connection()
blueprint = Blueprint('payments', __name__)

@blueprint.route('/payment', methods=['POST']) 
@expects_json(payment_schema)
def post():
    """Saves new payment
        Returns:
            200: txid
            500: error message
        """
        
    try:
        tx_id = request.json.get('tx_id')
        user_id = request.json.get('user_id')

        session.add(Payment(
            tx_id=tx_id,
            user_id=user_id,
        ))
        session.commit()  
        return 200
    except Exception as err:
        print(err)
        raise abort(500, description='Failed to create payment')
    
CORS(blueprint)

