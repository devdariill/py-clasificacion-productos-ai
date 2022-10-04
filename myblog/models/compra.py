# 35:20
import datetime
from email.policy import default
from myblog import db
from sqlalchemy.dialects.mysql import VARCHAR
from sqlalchemy import Float
from sqlalchemy.sql import sqltypes

# nuestra calse ya es un modelos
# se crea la tabla users con atributos id ...

# numcom, nomdoc, precom, docext, feccom, vencom, nitter, nomter, dirter, telter, corele, subcom, totiva, totcom, estcom, codemp,
# horcom, obscom, codclas, forpag, totdct, totaju


class Compra(db.Model):
    __tablename__ = "compras"
    numcom = db.Column(VARCHAR, primary_key=True)
    nomdoc = db.Column(VARCHAR, default="COMPRA")
    precom = db.Column(Float, default="")
    docext = db.Column(VARCHAR, default=numcom)
    feccom = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    vencom = db.Column(
        db.DateTime, default=datetime.datetime.utcnow+datetime.timedelta(days=30))
    nitter = db.Column(VARCHAR)
    nomter = db.Column(VARCHAR)
    dirter = db.Column(VARCHAR)
    telter = db.Column(VARCHAR)
    corele = db.Column(VARCHAR)
    subcom = db.Column(Float)
    totiva = db.Column(Float)
    totcom = db.Column(Float)
    estcom = db.Column(VARCHAR)
    codemp = db.column(VARCHAR, db.ForeignKey('users.id'))
    horcom = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    obscom = db.Column(VARCHAR)
    # TODO preguntar para que es foreing key
    codclas = db.Column(VARCHAR)
    forpag = db.Column(VARCHAR)
    totdct = db.Column(Float)
    totaju = db.Column(Float)

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

