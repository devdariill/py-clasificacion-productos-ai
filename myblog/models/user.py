#35:20
from myblog import db #

#nuestra calse ya es un modelos
    #se crea la tabla users con atributos id ...
class User(db.Model):
    __tablename__="users"
    id=db.Column(db.Integer,primary_key=True)
    username=db.Column(db.String(50))
    password=db.Column(db.Text)

    #visualizar datos uysuario creando un contructor
    def __init__(self,username,password) -> str:
        self.username = username
        self.password = password

    def __repr__(self) -> str:
        return f'User: {self.username}'


