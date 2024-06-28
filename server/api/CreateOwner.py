from flask import request, jsonify, render_template
from models import db, Owner  # Ensure Owner is imported
from werkzeug.security import generate_password_hash

def create_owner():
    if request.method == 'POST':
        try:
            data = request.form if request.form else request.json
            first_name = data.get('first_name')
            last_name = data.get('last_name')
            email = data.get('email')
            password = data.get('password')
            phone_number = data.get('phone_number')
            address = data.get('address')
            city = data.get('city')
            state = data.get('state')
            country = data.get('country')
            subscription_status = data.get('subscription_status', 'inactive')
            role = data.get('role', 'owner')

            # Validate required fields
            if not first_name or not last_name or not email or not password:
                return jsonify({"error": "Missing required fields"}), 400

            # Check if the email is already registered
            if Owner.query.filter_by(email=email).first():
                return jsonify({"error": "Email already registered"}), 400

            # Create a new owner
            password_hash = generate_password_hash(password)  # Generate password hash
            new_owner = Owner(
                first_name=first_name,
                last_name=last_name,
                email=email,
                password_hash=password_hash,
                phone_number=phone_number,
                address=address,
                city=city,
                state=state,
                country=country,
                subscription_status=subscription_status,
                role=role,
                is_active=True
            )
            db.session.add(new_owner)
            db.session.commit()

            return jsonify({"message": "Owner created successfully"}), 201

        except Exception as e:
            db.session.rollback()  # Rollback the session in case of an error
            return jsonify({"error": str(e)}), 500

    # Render a form for creating an owner (for HTML template use)
    if request.method == 'GET':
        return render_template('create_owner.html')
