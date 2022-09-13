from flask import Flask #
from flask_sqlalchemy import SQLAlchemy #


app=Flask(__name__)


#modo de desarrollo
app.config.from_object('config.DevelopmentConfig')
db=SQLAlchemy(app)

#importar vistas 53:35
from myblog.views.auth import auth
app.register_blueprint(auth)
#/

from myblog.views.productos import productos
app.register_blueprint(productos)

#2:06:07
# from myblog.views.blog import blog
# app.register_blueprint(blog)

db.create_all()