import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or '62e65014acfd20a10b7d6d4a2034cd8d64b7ba2c6ee10210'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'mysql+pymysql://root:habakkuk10tamunosakijacob@localhost/Finflow'
SQLALCHEMY_TRACK_MODIFICATIONS = False
JWT_SECRET_KEY = os.environ.get('JWT_SECRET_KEY') or '9459bf626aefd220092bf0cc3b94eacb7cb42e0e547d9ffa'