from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager

# Initialize the database
db = SQLAlchemy()

# Initialize the JWT Manager
jwt = JWTManager()

def create_app():
    app = Flask(__name__)

    # Load the configuration from config.py
    app.config.from_object('app.config.Config')

    # Initialize the extensions
    db.init_app(app)
    jwt.init_app(app)

    # Import models so they are registered with SQLAlchemy
    with app.app_context():
        from app.models import User, Account, Transaction

    # Register Blueprints (for routes)
    from app.routes.main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app
