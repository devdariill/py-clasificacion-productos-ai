#35:20
from myblog import db #
from datetime import  datetime #

#nuestra calse ya es un modelos
    #se crea la tabla users con atributos id ...
class Post(db.Model):
    __tablename__="posts"
    id=db.Column(db.Integer,primary_key=True)
    author = db.Column(db.Integer,db.ForeignKey('users.id'),nullable=False)
    title=db.Column(db.String(100))
    body=db.Column(db.Text)
    created = db.Column(db.DateTime,nullable=False,default=datetime.utcnow)


    #visualizar datos post creando un contructor
    def __init__(self,author,title,body) -> None:
        self.author = author
        self.title = title
        self.body = body

    def __repr__(self) -> str:
        return f'Post: {self.title}'