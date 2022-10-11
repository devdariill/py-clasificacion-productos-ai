#null
class Config:
    DEBUG=True
    TESTING=True

    #CONFIGURACION BASE DATOS 
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI="mysql+pymysql://root:@localhost:3306/remodelar"

class ProductionsConfig(Config):
    DEBUG= False

class DevelopmentConfig(Config):
    SECRET_KEY='dev'
    DEBUG=True
