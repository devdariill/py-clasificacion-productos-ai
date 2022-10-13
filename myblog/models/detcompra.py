from myblog import db
import datetime
from sqlalchemy.dialects.mysql import VARCHAR,DOUBLE

# numcom, codprod, codcon, nomdet, serdet, venfec, valuni, candet, ivapor, 
# ivapes, cosuni, totdet, numite, codclas, dctpor, undfra, reginv

class DetCompra(db.Model):
    __tablename__ = "detcompras"
    numcom = db.Column(db.String(20), db.ForeignKey('compras.numcom'),primary_key=True)    
    codprod = db.Column(db.String(20), db.ForeignKey('productos.codprod'),primary_key=True)
    codcon = db.Column(db.String(12))
    nomdet = db.Column(db.String(200))
    # serdet = db.Column(VARCHAR)
    venfec = db.Column(db.DateTime,default=datetime.datetime.utcnow)
    valuni = db.Column(db.Float, default=0)
    candet = db.Column(db.Float)
    ivapor = db.Column(db.Float)
    ivapes = db.Column(db.Float)
    cosuni = db.Column(db.Float)
    totdet = db.Column(db.Float)
    # TODO AUTO INCREMENTAL MAYBE FAIL
    numite = db.Column(db.Integer)
    codclas = db.Column(db.String(4))
    dctpor = db.Column(db.Float)
    undfra = db.Column(db.Integer)
    # reginv = db.Column(VARCHAR)

    # visualizar datos uysuario creando un contructor
    def __init__(self, numcom, codprod, nomdet, venfec, valuni, candet, ivapor, ivapes, cosuni, totdet, numite, codclas, dctpor, undfra, ) :
        self.numcom = numcom
        self.codprod = codprod
        self.codcon = ""
        self.nomdet = nomdet
        # self.serdet = serdet
        self.venfec = venfec
        self.valuni = valuni
        self.candet = candet
        self.ivapor = ivapor
        self.ivapes = ivapes
        self.cosuni = cosuni
        self.totdet = totdet
        self.numite = numite
        self.codclas = codclas
        self.dctpor = dctpor
        self.undfra = undfra
        # self.reginv = reginv


    def __repr__(self) -> str:
        return f'detCompra: {self.numcom}'

