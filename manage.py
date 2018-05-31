#!/usr/bin/env python
import os
from app import create_app, db
from app.model.contract import Contract,Bill,Repayment
from app.model.user import User

app = create_app(os.getenv('FLASK_CONFIG') or 'default')


if __name__ == '__main__':
    app.run(host="0.0.0.0",port=5500)
