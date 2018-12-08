#!/usr/bin/env python3
"""
main.py - Run the complete application
"""

from app import create_app
from db import create_db
from views import views

app = create_app()
db = create_db()
app.register_blueprint(views)


def run():
    app.run(host='0.0.0.0', port=5000, debug=True)

if __name__ == '__main__':
    run()
