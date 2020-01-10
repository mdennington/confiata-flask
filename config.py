import os
basedir = os.path.abspath(os.path.dirname(__file__))



class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or '123fghL69'
    MAIL_SERVER = os.environ.get('MAIL_SERVER', 'smtp.googlemail.com')
    MAIL_PORT = int(os.environ.get('MAIL_PORT', '587'))
    MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS', 'true').lower() in \
        ['true', 'on', '1']
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    CONFIATA_MAIL_SUBJECT_PREFIX = '[CONFIATA]'
    CONFIATA_MAIL_SENDER = 'Confiata Admin <info@confiata.org>'
    CONFIATA_ADMIN = os.environ.get('CONFIATA_ADMIN')

    @staticmethod
    def init_app(app):
        pass

# TODO Research best practices for Environment Vars
# TODO What do I need for dev, test and production for Mongo?
class DevelopmentConfig(Config):
    DEBUG = True
    MONGODB_SETTINGS = { 'db' : 'confiata'}


class TestingConfig(Config):
    TESTING = True
    MONGODB_SETTINGS = { 'db' : 'confiata'}


class ProductionConfig(Config):
    MONGODB_SETTINGS = { 'db' : 'confiata'}


config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,

    'default': DevelopmentConfig
}
