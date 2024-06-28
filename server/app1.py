from flask import Flask
from werkzeug.security import generate_password_hash  # for password hashing
#from flask_sqlalchemy import SQLAlchemy

from config import Config
import logging
from flask_cors import CORS
import psycopg2
from login1 import login
from CreateCust import create_cust
app = Flask(__name__)
app.config.from_object(Config)

CORS(app)  # Allow CORS for all routes (suitable for development)

#db = SQLAlchemy(app)  # Initialize database with the app
#from models import Customer
from CreateOwner import create_owner  # Import the create_owner function
from flask_migrate import Migrate
from models import db, bcrypt

#db.init_app(app)
bcrypt.init_app(app)
migrate = Migrate(app, db)
    # ... other model attributes and methods (if needed)
@app.route('/login', methods=['GET','POST'])
def login_route():
    return login()
@app.route('/create-user', methods=['GET','POST'])
def create_user():
    return create_cust(db)

@app.route('/create-owner', methods=['GET', 'POST'])
def create_owner_route():
    return create_owner()

# Create database tables (if they don't exist)
#with app.app_context():
 #   db.create_all()

if __name__ == '__main__':
    app.run(debug=True)  # Set debug to False in production
