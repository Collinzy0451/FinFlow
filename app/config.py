import os

class Config:
    SECRET_KEY = os.environ.get('09053361954')
    SQLALCHEMY_DATABASE_URI = os.environ.get('mysql+pymysql://root:habakkuk10tamunosakijacob@localhost/Finflow')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JWT_SECRET_KEY = os.environ.get('8c529d482e6f644f725da2726603befa1503a950c91925c4')
