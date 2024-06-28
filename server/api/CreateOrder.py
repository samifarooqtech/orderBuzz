from flask import request, jsonify, render_template
from models import db, Order  # Ensure Order is imported

def create_order():
    if request.method == 'POST':
        try:
            data = request.form if request.form else request.json
            restaurant_id = data.get('restaurant_id')
            owner_id = data.get('owner_id')
            customer_name = data.get('customer_name')
            phone_number = data.get('phone_number')
            order_status = data.get('order_status', 'Pending')
            other_order_details = data.get('other_order_details', '')

            # Validate required fields
            if not restaurant_id or not owner_id or not customer_name or not phone_number:
                return jsonify({"error": "Missing required fields"}), 400

            # Create a new order
            new_order = Order(
                restaurant_id=restaurant_id,
                owner_id=owner_id,
                customer_name=customer_name,
                phone_number=phone_number,
                order_status=order_status,
                other_order_details=other_order_details
            )
            db.session.add(new_order)
            db.session.commit()

            return jsonify({"message": "Order created successfully"}), 201

        except Exception as e:
            db.session.rollback()  # Rollback the session in case of an error
            return jsonify({"error": str(e)}), 500

    # Render a form for creating an order (for HTML template use)
    if request.method == 'GET':
        return render_template('create_order.html')
