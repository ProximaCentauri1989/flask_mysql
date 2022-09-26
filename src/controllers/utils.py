from werkzeug.exceptions import HTTPException

def abort(code, description=None):
    ex = HTTPException(description=description)
    ex.code=code
    raise ex
