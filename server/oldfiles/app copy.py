from flask import Flask, request, jsonify
from flask_bcrypt import Bcrypt
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from config import Config
import logging


from message_handler import get_message  # Import the function

app = Flask(__name__)
app.config.from_object(Config)
##print(app)
CORS(app)  # Allow CORS for all routes (suitable for development)

#app = Flask(__name__)
bcrypt = Bcrypt(app)
db = SQLAlchemy(app)

logging.basicConfig()
logging.getLogger('sqlalchemy.engine').setLevel(logging.INFO)

# Import models here to avoid circular imports
from models import Customer

# Replace with your actual user data (hashed passwords)
users = {
    'user1': {'password': bcrypt.generate_password_hash('password123'.encode('utf-8')).decode('utf-8')},
}

@app.route('/get-message')
def get_message_wrapper():
    return get_message()
@app.route('/create-user', methods=['GET','POST'])
def create_user():
    try:
        new_user = Customer(username="John", password="john123")

        # Add the user to the database
        db.session.add(new_user)
        db.session.commit()
    except Exception as e:
        return jsonify({"message": str(e)}), 500
    
@app.route('/create-db', methods=['GET', 'POST'])
def create_db():
    try:
        db.create_all()
        return jsonify({"message": "Database created successfully!"}), 201
    except Exception as e:
        return jsonify({"message": str(e)}), 500
    

@app.route('/check-table')
def check_table():
    try:
        db.reflect()
        if 'user' in db.metadata.tables:
            return jsonify({"message": "User table exists"}), 200
        else:
            return jsonify({"message": "User table does not exist"}), 404
    except Exception as e:
        return jsonify({"message": str(e)}), 500

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()

    if not data or not data.get('username') or not data.get('password'):
        return jsonify({'message': 'Missing username or password'}), 400

    username = data['username']
    password = data['password']
    print('Received username:', username) 
    print('Received password:', password)
    if username in users and bcrypt.check_password_hash(users[username]['password'], password.encode('utf-8')):
        print("Success")
        return jsonify({'message': 'Login successful'}), 200
    else:
        print("Failed")
        return jsonify({'message': 'Invalid username or password'}), 401

if __name__ == '__main__':
    app.run(debug=True)
