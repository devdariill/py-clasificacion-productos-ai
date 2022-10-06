from myblog import db
from sqlalchemy.dialects.mysql import VARCHAR,CHAR

# numcom, codprod, codcon, nomdet, serdet, venfec, valuni, candet,
# ivapor, ivapes, cosuni, totdet, numite, codclas, dctpor, undfra, reginv

class Producto(db.Model):
    __tablename__ = "detcompras"
    numcom = db.Column(VARCHAR, db.ForeignKey('compras.numcom'))    
    codprod = db.Column(VARCHAR, db.ForeignKey('productos.codprod'))
    codbar = db.Column(VARCHAR, default=codprod)
    nomprod = db.Column(VARCHAR)
    exiprod = db.Column(Float, default=0)
    tipcos = db.Column(sqltypes.CHAR)
    cosprod = db.Column(Float)
    # cosaut=db.Column(Float)
    # cosulc=db.Column(db.String)
    fecapa = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    venprod = db.Column(Float)
    undfra = db.Column(Float, default=1)
    pvenfra = db.Column(Float)

    # visualizar datos uysuario creando un contructor
    def __init__(self, codprod, codbar, nomprod, exiprod, cosprod, venprod, undfra, pvenfra) -> str:
        self.codprod = codprod
        self.codbar = codbar
        self.nomprod = nomprod
        self.exiprod = exiprod
        self.tipcos = "UC"
        self.cosprod = cosprod
        self.venprod = venprod
        self.undfra = undfra
        self.pvenfra = pvenfra

    def __repr__(self) -> str:
        return f'Producto: {self.nomprod}'
