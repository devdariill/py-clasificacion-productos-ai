from flask import Flask #
from flask_sqlalchemy import SQLAlchemy #

app=Flask(__name__)
# app.secret_key = 'ronald'

app.config.from_object('config.DevelopmentConfig')
db=SQLAlchemy(app)

from myblog.views.auth import auth
app.register_blueprint(auth)

from myblog.views.productos import productos
app.register_blueprint(productos)

db.create_all()