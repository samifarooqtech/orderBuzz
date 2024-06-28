from app import db, bcrypt, User

db.create_all()

# Create a test user
hashed_password = bcrypt.generate_password_hash('password123').decode('utf-8')
new_user = Customer(username='testuser', password=hashed_password)
db.session.add(new_user)
db.session.commit()