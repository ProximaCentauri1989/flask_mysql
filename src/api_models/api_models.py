from apiflask import Schema
from apiflask.fields import String, Integer, List, Nested
from apiflask.validators import Length

class UserIn(Schema):
    username = String(required=True, validate=Length(0, 64))
    email = String(required=True)
    password = String(required=True, validate=Length(0, 128))
    
class UserOut(Schema):
    id = Integer()
    username = String(required=True, validate=Length(0, 64))
    email = String(required=True)
    
class APIResponseBaseReduced(Schema):
    result = String()
    
class APIResponseGetUsers(Schema):
    data = List(Nested(UserOut))
