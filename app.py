#!/usr/bin/env python
from flask import json
from flask import render_template
from werkzeug.exceptions import HTTPException
from src import app
from src.controllers import users_api, payments_api

@app.errorhandler(HTTPException)
def handle_http_exception(e):
    """Return JSON instead of HTML for HTTP errors."""
    response = e.get_response()
    response.data = json.dumps({
        "code": e.code,
        "detail": e.description,
    })
    response.content_type = "application/json"
    return response

def run_app():
    app.register_blueprint(users_api.blueprint, url_prefix='/api')
    app.register_blueprint(payments_api.blueprint, url_prefix='/api')
    app.run(debug=True, host='0.0.0.0')

if __name__ == '__main__':
    run_app()
