from flask import Flask
from flask_cors import CORS
from config import Config
from models import db
from flask_migrate import Migrate

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    CORS(app)  # Allow CORS for all routes (suitable for development)

    db.init_app(app)  # Initialize database with the app
    migrate = Migrate(app, db)  # Initialize Flask-Migrate

    from api import api_bp
    app.register_blueprint(api_bp, url_prefix='/api')  # Register the blueprint with a URL prefix

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
