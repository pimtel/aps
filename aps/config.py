import os

class Config:
    DEBUG = False
    TESTING = False
    # SQLALCHEMY_DATABASE_URI = 'sqlite://:memory/:'
    API_TITLE = 'APS'
    API_VERSION = 'v1'
    OPENAPI_VERSION = '3.0.2'

class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = f'postgres://{os.getenv("DATABASE_USERNAME")}:{os.getenv("DATABASE_PASSWORD")}@localhost:5432/aps'
    FLASK_ENV = "production"

class DevelopmentConfig(Config):
    FLASK_ENV = "development"
    DEBUG = True

class TestingConfig(Config):
    FLASK_ENV = "testing"
    TESTING = True
