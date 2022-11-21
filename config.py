

class Config:
    pass


class ProdConfig(Config):
    DEBUG=True
    SQLALCHEMY_DATABASE_URI='postgresql://postgres:root@localhost:5432/bookstore4'

class DevConfig(Config):
    DEBUG=True
    SQLALCHEMY_DATABASE_URI='postgresql://postgres:root@localhost:5432/bookstore4'



app_config = {
    'dev': DevConfig,
    'prod': ProdConfig
}