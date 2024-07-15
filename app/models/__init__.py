from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# Import all models here to register them with SQLAlchemy
from .user import User
from .account import Account
from .transaction import Transaction