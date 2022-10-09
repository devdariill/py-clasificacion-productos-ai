# 35:20
import datetime
from email.policy import default
from myblog import db
from sqlalchemy.dialects.mysql import VARCHAR,DOUBLE
# from sqlalchemy import Float
from sqlalchemy.sql import sqltypes

# nuestra calse ya es un modelos
# se crea la tabla users con atributos id ...


class Producto(db.Model):
    __tablename__ = "productos"
    codprod = db.Column(VARCHAR, primary_key=True)
    codbar = db.Column(VARCHAR, default=codprod)
    nomprod = db.Column(VARCHAR)
    exiprod = db.Column(DOUBLE, default=0)
    tipcos = db.Column(sqltypes.CHAR)
    # cosprod = db.Column(VARCHAR)
    # cosaut=db.Column(VARCHAR)
    venprod = db.Column(DOUBLE)
    cosulc=db.Column(DOUBLE)
    fecapa = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    undfra = db.Column(db.Integer, default=1)
    pvenfra = db.Column(DOUBLE,default=0)

    # visualizar datos uysuario creando un contructor
    def __init__(self, codprod, codbar, nomprod, exiprod,cosulc, venprod, undfra, pvenfra) -> None:
        self.codprod = codprod
        self.codbar = codbar
        self.nomprod = nomprod
        self.exiprod = exiprod
        self.tipcos = "UC"
        # self.cosprod = cosprod
        # self.cosaut = cosaut
        self.cosulc = cosulc
        self.venprod = venprod
        self.undfra = undfra
        self.pvenfra = pvenfra

    def __repr__(self) -> str:
        return f'Producto: {self.nomprod}'


"""
codprod, codbar, nomprod, exiprod, tipcos, cosprod, cosaut, cosulc, venprod, pvenfra
"""
