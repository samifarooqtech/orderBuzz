from flask import Flask, request, jsonify
from werkzeug.security import generate_password_hash  # for password hashing
from flask_sqlalchemy import SQLAlchemy

from config import Config
import logging

# Database configuration (replace with your details)
app = Flask(__name__)
#app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:sami123@localhost:5432/mydatabase'
#app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config.from_object(Config)
db = SQLAlchemy(app)  # Initialize database with the app
from models import Customer
"""
class Customer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)
"""
    # ... other model attributes and methods (if needed)

@app.route('/create-user', methods=['GET','POST'])
def create_user():
    try:
        # Extract username and password from request data
        #data = request.get_json()
        username ="sami2" #data.get('username')
        password = "Sami" #data.get('password')

        # Validate data (optional)
        if not username or not password:
            return jsonify({'error': 'Missing username or password'}), 400

        # Hash the password before storing (security best practice)
        hashed_password = generate_password_hash(password)

        # Create a new customer object
        customer = Customer(username=username, password_hash=hashed_password)

        # Add the customer to the database session
        db.session.add(customer)

        # Commit the changes to the database
        db.session.commit()

        return jsonify({'message': 'User created successfully!'}), 201

    except Exception as e:
        print(f"Error creating user: {e}")
        db.session.rollback()  # Rollback database changes on error
        return jsonify({'error': 'Failed to create user'}), 500

# Create database tables (if they don't exist)
with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=False)  # Set debug to False in production
