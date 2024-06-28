from flask import request, jsonify, render_template
from models import db, Customer  # Ensure Customer is imported

def create_customer():
    if request.method == 'POST':
        try:
            data = request.form if request.form else request.json
            customer_name = data.get('customer_name')
            phone_number = data.get('phone_number')
            restaurant_id = data.get('restaurant_id')
            owner_id = data.get('owner_id')

            # Validate required fields
            if not customer_name or not phone_number or not restaurant_id or not owner_id:
                return jsonify({"error": "Missing required fields"}), 400

            # Create a new customer
            new_customer = Customer(
                customer_name=customer_name,
                phone_number=phone_number,
                restaurant_id=restaurant_id,
                owner_id=owner_id
            )
            db.session.add(new_customer)
            db.session.commit()

            return jsonify({"message": "Customer created successfully"}), 201

        except Exception as e:
            db.session.rollback()  # Rollback the session in case of an error
            return jsonify({"error": str(e)}), 500

    # Render a form for creating a customer (for HTML template use)
    if request.method == 'GET':
        return render_template('create_customer.html')
