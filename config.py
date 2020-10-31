import os

class Config:
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:Raykip254@localhost/blog'
    SECRET_KEY =os.environ.get('SECRET_KEY')
   
   

    #  email configurations
  
    


class ProdConfig(Config):
   pass


class TestConfig(Config):
    
    DEBUG = True

class DevConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:Raykip254@localhost/blog'
    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig
}