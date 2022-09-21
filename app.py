#!/usr/bin/env python
from src import app

def run_app():
    app.run(debug=True, host='0.0.0.0')

if __name__ == '__main__':
    run_app()
