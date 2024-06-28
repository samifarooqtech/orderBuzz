# auth.py
from flask import request, jsonify
from werkzeug.security import check_password_hash
from config import Config  # Assuming Config is defined in config.py

def login():
    print("entering in login")
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
