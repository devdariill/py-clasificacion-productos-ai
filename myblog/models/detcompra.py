from myblog import db
import datetime
from sqlalchemy.dialects.mysql import VARCHAR,DOUBLE

# numcom, codprod, codcon, nomdet, serdet, venfec, valuni, candet, ivapor, 
# ivapes, cosuni, totdet, numite, codclas, dctpor, undfra, reginv

class DetCompra(db.Model):
    __tablename__ = "detcompras"
    numcom = db.Column(VARCHAR, db.ForeignKey('compras.numcom'),primary_key=True)    
    codprod = db.Column(VARCHAR, db.ForeignKey('productos.codprod'))
    codcon = db.Column(VARCHAR)
    nomdet = db.Column(VARCHAR)
    # serdet = db.Column(VARCHAR)
    venfec = db.Column(db.DateTime,default=datetime.datetime.utcnow)
    valuni = db.Column(VARCHAR  )
    candet = db.Column(VARCHAR)
    ivapor = db.Column(db.Float)
    ivapes = db.Column(VARCHAR)
    cosuni = db.Column(VARCHAR)
    totdet = db.Column(VARCHAR)
    # TODO AUTO INCREMENTAL MAYBE FAIL
    numite = db.Column(db.Integer)
    codclas = db.Column(VARCHAR)
    dctpor = db.Column(VARCHAR)
    undfra = db.Column(db.Integer)
    # reginv = db.Column(VARCHAR)

    # visualizar datos uysuario creando un contructor
    def __init__(self, numcom, codprod, nomdet, venfec, valuni, candet, ivapor, ivapes, cosuni, totdet, numite, codclas, dctpor, undfra, ) -> None:
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

