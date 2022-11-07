from flask import Flask #
from flask_sqlalchemy import SQLAlchemy #
# from sqlalchemy import create_engine

app=Flask(__name__)
app.config.from_object('config.DevelopmentConfig')
db=SQLAlchemy(app)
with app.app_context():
    db.create_all()


# app.secret_key = 'ronald'

#TODO CHECK THIS
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

# engine= create_engine(app.config.from_object('config.DevelopmentConfig'))
# session=db.session()
# cursos=session.execute("select * from users").cursor.fetchall()
# print(cursos)

# session=db.session()    
# cursos=session.execute(
#     f"select * from terceros where nitter = '{id}'"
# ).cursor.fetchall()
# tercero = cursos[0]
# print(tercero)

from myblog.views.auth import auth
app.register_blueprint(auth)

from myblog.views.productos import productos
app.register_blueprint(productos)

from myblog.views.compras import compras
app.register_blueprint(compras)

from myblog.views.ventas import ventas
app.register_blueprint(ventas)

