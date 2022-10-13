from myblog import db
from sqlalchemy.dialects.mysql import VARCHAR,CHAR


# nitter, tipnit, perjur, razsoc, apeter, apeter2, nomter, nomter2, nomcom, dirter, telter, corele, cliter, proter, empter, actter

class Tercero(db.Model):
    __tablename__ = "terceros"
    nitter = db.Column(db.String(15), primary_key=True)
    tipnit = db.Column(db.String(25), default="Nit")
    perjur = db.Column(db.String(10), default="NATURAL")
    razsoc = db.Column(db.String(100), default="")
    apeter = db.Column(db.String(100), default="")
    apeter2 = db.Column(db.String(100), default="")
    nomter = db.Column(db.String(100), default="")
    nomter2 = db.Column(db.String(100), default="")
    nomcom = db.Column(db.String(100), default="")
    dirter = db.Column(db.String(50), default="")
    telter = db.Column(db.String(50), default="")
    corele = db.Column(db.String(150), default="")
    cliter = db.Column(db.String(2), default="")
    proter = db.Column(db.String(2), default="")
    empter = db.Column(db.String(2), default="") 
    actter = db.Column(db.String(1), default="N")

    def __init__(self, nitter, tipnit, perjur, razsoc, apeter, apeter2, nomter, nomter2, nomcom, dirter, telter, corele, cliter, proter, empter, actter) :
        self.nitter = nitter
        self.tipnit = tipnit
        self.perjur = perjur
        self.razsoc = razsoc
        self.apeter = apeter
        self.apeter2 = apeter2
        self.nomter = nomter
        self.nomter2 = nomter2
        self.nomcom = nomcom
        self.dirter = dirter
        self.telter = telter
        self.corele = corele
        self.cliter = cliter
        self.proter = proter
        self.empter = empter
        self.actter = actter

    def __repr__(self) -> str:
        return f'Tercero: {self.nitter}'

