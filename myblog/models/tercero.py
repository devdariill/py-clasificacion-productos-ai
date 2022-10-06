from myblog import db
from sqlalchemy.dialects.mysql import VARCHAR,CHAR


# nitter, tipnit, perjur, razsoc, apeter, apeter2, nomter, nomter2, nomcom, dirter, telter, corele, cliter, proter, empter, actter

class Tercero(db.Model):
    __tablename__ = "terceros"
    nitter = db.Column(VARCHAR, primary_key=True)
    tipnit = db.Column(VARCHAR, default="Nit")
    perjur = db.Column(VARCHAR, default="NATURAL")
    razsoc = db.Column(VARCHAR, default="")
    apeter = db.Column(VARCHAR, default="")
    apeter2 = db.Column(VARCHAR, default="")
    nomter = db.Column(VARCHAR, default="")
    nomter2 = db.Column(VARCHAR, default="")
    nomcom = db.Column(VARCHAR, default="")
    dirter = db.Column(VARCHAR, default="")
    telter = db.Column(VARCHAR, default="")
    corele = db.Column(VARCHAR, default="")
    cliter = db.Column(CHAR, default="")
    proter = db.Column(CHAR, default="")
    empter = db.Column(CHAR, default="") 
    actter = db.Column(CHAR, default="N")

    def __init__(self, nitter, tipnit, perjur, razsoc, apeter, apeter2, nomter, nomter2, nomcom, dirter, telter, corele, cliter, proter, empter, actter) -> str:
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

