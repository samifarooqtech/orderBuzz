from flask import Flask, request, jsonify
from werkzeug.security import generate_password_hash  # for password hashing
from werkzeug.security import check_password_hash
from flask_sqlalchemy import SQLAlchemy

from config import Config
import logging
from flask_cors import CORS
import psycopg2
app = Flask(__name__)
app.config.from_object(Config)

CORS(app)  # Allow CORS for all routes (suitable for development)

db = SQLAlchemy(app)  # Initialize database with the app
from models import Customer

    # ... other model attributes and methods (if needed)
@app.route('/login', methods=['GET','POST'])
def login():
    try:
        username = request.get_json().get('username')
        password = request.get_json().get('password')
       

        # Validate data (optional)
        if not username or not password:
            return jsonify({'error': 'Missing username or password'}), 400

        # Check if username exists in database using PostgreSQL cursor
        conn = Config.establish_db_connection()
        cur = conn.cursor()
        cur.execute("SELECT password_hash FROM customer WHERE username = %s", (username,))
        user_data = cur.fetchone()
        conn.close()  # Close the connection after use

        if not user_data:
            print('Invalid username or password')
            return jsonify({'error': 'Invalid username or password'}), 401

        # Validate password hash using werkzeug.security.check_password_hash
        if not check_password_hash(user_data[0], password):
            print('Invalid username or password')
            return jsonify({'error': 'Invalid username or password'}), 401

        return jsonify({'message': 'Login successful!'}), 200

    except Exception as e:
        print(f"Error during login: {e}")
        return jsonify({'error': 'An error occurred. Please check username and password and try again.'}), 500


@app.route('/create-user', methods=['GET','POST'])
def create_user():
    try:
        # Extract username and password from request data
        print('Enter create user')
        data = request.get_json()
        username = data.get('username')
        password = data.get('password')
        firstName = request.get_json().get('firstName')
        lastName = request.get_json().get('lastName')
        email = request.get_json().get('email')
        phone = request.get_json().get('phone')
        
       
        # Validate data (optional)
        if not username or not password:
            return jsonify({'error': 'Missing username or password'}), 400

        # Hash the password before storing (security best practice)
        hashed_password = generate_password_hash(password)

        # Create a new customer object
        customer = Customer(username=username, password_hash=hashed_password,
                           first_name=firstName,
                            last_name=lastName,
                             email=email,
                              phone=phone )

        print(customer)
        # Add the customer to the database session
        db.session.add(customer)

        # Commit the changes to the database
        db.session.commit()

        return jsonify({'message': 'User created successfully!'}), 201

    except Exception as e:
        print(f"Error creating user: {e}")
        db.session.rollback()  # Rollback database changes on error
        return jsonify({'error': 'Failed to create user****'}), 500

# Create database tables (if they don't exist)
with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)  # Set debug to False in production
