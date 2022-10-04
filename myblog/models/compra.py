# 35:20
import datetime

from myblog import db
from sqlalchemy.dialects.mysql import VARCHAR

# nuestra calse ya es un modelos
# se crea la tabla users con atributos id ...

# numcom, nomdoc, precom, docext, feccom, vencom, nitter, nomter, dirter, telter, corele, subcom, totiva, totcom, estcom, codemp,
# horcom, obscom, codclas, forpag, totdct, totaju


class Compra(db.Model):
    __tablename__ = "compras"
    numcom = db.Column(db.Integer, primary_key=True)
    nomdoc = db.Column(db.Integer, default="COMPRA")
    precom = db.Column(db.Integer, default="")
    docext = db.Column(db.Integer, default=numcom)
    feccom = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    #TODO fecha de vencimiento
    vencom = db.Column(db.DateTime,
                       default=datetime.datetime.utcnow)
    nitter = db.Column(db.Integer)
    nomter = db.Column(db.Integer)
    dirter = db.Column(db.Integer)
    telter = db.Column(db.Integer)
    corele = db.Column(db.Integer)
    subcom = db.Column(VARCHAR)
    totiva = db.Column(VARCHAR)
    totcom = db.Column(VARCHAR)
    estcom = db.Column(db.String(1), default="B")
    codemp = db.column(VARCHAR, db.ForeignKey('users.id'))
    #TODO preguntar por horcom
    horcom = db.Column(db.Integer)
    obscom = db.Column(db.String(100))
    # TODO preguntar para que es foreing key
    codclas = db.Column(db.String,default="S18")
    forpag = db.Column(db.String(1), default="E")
    totdct = db.Column(VARCHAR)
    totaju = db.Column(VARCHAR)

    def __init__(self, numcom, nomdoc, precom, docext, feccom, vencom, nitter, nomter, dirter, telter, corele, subcom,
                totiva, totcom, estcom, codemp, horcom, obscom, codclas, forpag, totdct, totaju) -> str:
        self.numcom = numcom
        self.nomdoc = nomdoc
        self.precom = precom
        self.docext = docext
        self.feccom = feccom
        self.vencom = vencom
        self.nitter = nitter
        self.nomter = nomter
        self.dirter = dirter
        self.telter = telter
        self.corele = corele
        self.subcom = subcom
        self.totiva = totiva
        self.totcom = totcom
        self.estcom = estcom
        self.codemp = codemp
        self.horcom = horcom
        self.obscom = obscom
        self.codclas = codclas
        self.forpag = forpag
        self.totdct = totdct
        self.totaju = totaju

    def __repr__(self) -> str:
        return f'Compra: {self.numcom}'

