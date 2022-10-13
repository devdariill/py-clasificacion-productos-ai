# 35:20
import datetime
from email.policy import default
from myblog import db
from sqlalchemy.dialects.mysql import VARCHAR
# from sqlalchemy import Float
from sqlalchemy.sql import sqltypes

# nuestra calse ya es un modelos
# se crea la tabla users con atributos id ...


class Producto(db.Model):
    __tablename__ = "productos"
    codprod = db.Column(db.String(20), primary_key=True)
    codbar = db.Column(db.String(30), default=codprod)
    nomprod = db.Column(db.String(100))
    exiprod = db.Column(db.Float, default=0)
    tipcos = db.Column(db.String(2), default="UC")
    # cosprod = db.Column(VARCHAR)
    # cosaut=db.Column(VARCHAR)
    # ivainc=db.Column(db.string(1),default="N")
    venprod = db.Column(db.Float, default=0)
    cosulc=db.Column(db.Float, default=0)
    fecapa = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    undfra = db.Column(db.Integer, default=1)
    pvenfra = db.Column(db.Integer,default=0)

    # visualizar datos uysuario creando un contructor
    def __init__(self, codprod, codbar, nomprod, exiprod,cosulc, venprod, undfra, pvenfra) :
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
