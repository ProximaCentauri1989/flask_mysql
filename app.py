#!/usr/bin/env python
from src import app
from src.controllers import users_api

def run_app():
    app.register_blueprint(users_api.blueprint, url_prefix='/api')
    app.run(debug=True, host='0.0.0.0')

if __name__ == '__main__':
    run_app()
