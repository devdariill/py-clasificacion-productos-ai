# 35:20
import datetime
from email.policy import default

from myblog import db
from sqlalchemy.dialects.mysql import VARCHAR

# nuestra calse ya es un modelos
# se crea la tabla users con atributos id ...



# numcom, nomdoc, precom, docext, feccom, vencom, nitter, nomter, dirter, 
# telter, corele, subcom, totiva, totcom, estcom, codemp, horcom, obscom,
# codclas, forpag, totdct, totaju

#TODO CHANGE CARCHAR TO FLOAT
class Compra(db.Model):
    __tablename__ = "compras"
    numcom = db.Column(VARCHAR, primary_key=True)
    nomdoc = db.Column(VARCHAR, default="COMPRA")
    precom = db.Column(VARCHAR, default="")
    docext = db.Column(VARCHAR, default=numcom)
    feccom = db.Column(db.DateTime,default=datetime.datetime.utcnow)
    vencom = db.Column(db.DateTime,default=datetime.datetime.utcnow)
    nitter = db.Column(VARCHAR,db.ForeignKey('terceros.nitter'),default="")
    nomter = db.Column(VARCHAR,default="")
    dirter = db.Column(VARCHAR,default="")
    telter = db.Column(VARCHAR,default="")
    corele = db.Column(VARCHAR,default="")    
    subcom = db.Column(VARCHAR, default=0) 
    totiva = db.Column(VARCHAR,default="")
    totcom = db.Column(VARCHAR,default="")
    estcom = db.Column(db.String(1), default="B")
    codemp = db.Column(VARCHAR, db.ForeignKey('users.id'))
    horcom = db.Column(VARCHAR,default="24")
    obscom = db.Column(db.String(100))
    codclas = db.Column(db.String, default="S18")
    forpag = db.Column(db.String(1), default="E")
    totdct = db.Column(VARCHAR,default="")
    totaju = db.Column(VARCHAR,default="")

    def __init__(self, numcom, precom, docext, feccom, vencom, nitter, nomter, dirter, 
                telter, corele, subcom,totiva, totcom, estcom, codemp, horcom, obscom, 
                codclas, forpag, totdct, totaju) :
        self.numcom = numcom
        self.nomdoc = "COMPRA"
        self.precom = ""
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

