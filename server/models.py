from flask_sqlalchemy import SQLAlchemy

app = None  # Placeholder for Flask app instance (set later)
db = SQLAlchemy(app)  # Initialize with the app later (after app is created)

class Customer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)
    email = db.Column(db.String(255), unique=True, nullable=False)
    first_name = db.Column(db.String(80), nullable=False)
    last_name = db.Column(db.String(80), nullable=False)
    phone = db.Column(db.String(20), nullable=True)

    # ... other model attributes and methods (if needed)
