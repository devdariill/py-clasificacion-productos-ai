from flask import Flask #
from flask_sqlalchemy import SQLAlchemy #
# from sqlalchemy import create_engine

app=Flask(__name__)
# app.secret_key = 'ronald'

app.config.from_object('config.DevelopmentConfig')
db=SQLAlchemy(app)

# engine= create_engine(app.config.from_object('config.DevelopmentConfig'))
# session=db.session()
# cursos=session.execute("select * from users").cursor.fetchall()
# print(cursos)


from myblog.views.auth import auth
app.register_blueprint(auth)

from myblog.views.productos import productos
app.register_blueprint(productos)

db.create_all()