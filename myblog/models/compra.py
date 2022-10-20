# 35:20
import datetime
from myblog import db

# nuestra calse ya es un modelos
# se crea la tabla users con atributos id ...



# numcom, nomdoc, precom, docext, feccom, vencom, nitter, nomter, dirter, 
# telter, corele, subcom, totiva, totcom, estcom, codemp, horcom, obscom,
# codclas, forpag, totdct, totaju

#TODO CHANGE CARCHAR TO FLOAT
class Compra(db.Model):
    __tablename__ = "compras"
    numcom = db.Column(db.String(20), primary_key=True)
    nomdoc = db.Column(db.String(50), default="COMPRA")
    precom = db.Column(db.String(10), default="")
    docext = db.Column(db.String(20), default=numcom)
    feccom = db.Column(db.DateTime,default=datetime.datetime.utcnow)
    vencom = db.Column(db.DateTime,default=datetime.datetime.utcnow)
    nitter = db.Column(db.String(15),db.ForeignKey('terceros.nitter'),default="")
    nomter = db.Column(db.String(100),default="")
    dirter = db.Column(db.String(100),default="")
    telter = db.Column(db.String(50),default="")
    corele = db.Column(db.String(150),default="")    
    subcom = db.Column(db.Float, default=0) 
    totiva = db.Column(db.Float,default="")
    totcom = db.Column(db.Float,default="")
    estcom = db.Column(db.String(1), default="B")
    codemp = db.Column(db.String(15), db.ForeignKey('users.id'))
    #TODO FIX HORA COMPRA ACTUAL
    horcom = db.Column(db.Integer,default="24")
    obscom = db.Column(db.String(100))
    codclas = db.Column(db.String(4), default="S18")
    forpag = db.Column(db.String(1), default="E")
    totdct = db.Column(db.Float,default="")
    totaju = db.Column(db.Float,default="")

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

