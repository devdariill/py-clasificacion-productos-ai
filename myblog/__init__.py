from flask import Flask #
from flask_sqlalchemy import SQLAlchemy #
# from sqlalchemy import create_engine

app=Flask(__name__)
# app.secret_key = 'ronald'

app.config.from_object('config.DevelopmentConfig')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db=SQLAlchemy(app)

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

db.create_all()