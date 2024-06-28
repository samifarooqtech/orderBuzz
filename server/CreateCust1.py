# auth.py
from flask import request, jsonify
from werkzeug.security import generate_password_hash
from config import Config  # Assuming Config is defined in config.py
from models import db, Customer  # Assuming models.py contains your SQLAlchemy models

def create_cust(db):
    try:
        # Extract username and password from request data
        print('Enter create user')
        data = request.get_json()
        username = data.get('username')
        password = data.get('password')
        firstName = data.get('firstName')
        lastName = data.get('lastName')
        email = data.get('email')
        phone = data.get('phone')
        
        # Validate data (optional)
        if not username or not password:
            return jsonify({'error': 'Missing username or password'}), 400

        # Hash the password before storing (security best practice)
        hashed_password = generate_password_hash(password)

        # Create a new customer object
        customer = Customer(username=username, password_hash=hashed_password,
                            first_name=firstName, last_name=lastName, 
                            email=email, phone=phone)

        print(customer)
        # Add the customer to the database session
        db.session.add(customer)

        # Commit the changes to the database
        db.session.commit()

        return jsonify({'message': 'User created successfully!'}), 201

    except Exception as e:
        print(f"Error creating user: {e}")
        db.session.rollback()  # Rollback database changes on error
        return jsonify({'error': 'Failed to create user'}), 500
