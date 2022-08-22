#35:20
from myblog import db #
from sqlalchemy.dialects.mysql import VARCHAR
from sqlalchemy import Float
from sqlalchemy.sql import sqltypes

#nuestra calse ya es un modelos
    #se crea la tabla users con atributos id ...
class Producto(db.Model):
    __tablename__="productos"
    codprod=db.Column(VARCHAR,primary_key=True)
    codbar=db.Column(VARCHAR)
    nomprod=db.Column(VARCHAR)
    exiprod=db.Column(Float)
    tipcos=db.Column(sqltypes.CHAR)
    cosprod=db.Column(Float)
    # cosaut=db.Column(Float)
    # cosulc=db.Column(db.String)
    venprod=db.Column(Float)
    pvenfra=db.Column(Float)   
    

    #visualizar datos uysuario creando un contructor
    def __init__(self,codprod, codbar, nomprod, exiprod, cosprod, venprod, pvenfra ) -> str:
        self.codprod=codprod
        self.codbar =codbar
        self.nomprod=nomprod
        self.exiprod=exiprod
        self.tipcos="UC"
        self.cosprod=cosprod
        self.venprod=venprod
        self.pvenfra=pvenfra

    def __repr__(self) -> str:
        return f'Producto: {self.nomprod}'


"""
codprod, codbar, nomprod, exiprod, tipcos, cosprod, cosaut, cosulc, venprod, pvenfra
"""