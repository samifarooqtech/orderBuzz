from flask import request, jsonify, render_template
from models import db, Payment  # Ensure Payment is imported

def create_payment():
    if request.method == 'POST':
        try:
            data = request.form if request.form else request.json
            subscription_id = data.get('subscription_id')
            amount = data.get('amount')
            payment_date = data.get('payment_date')
            payment_method = data.get('payment_method')
            status = data.get('status')

            # Validate required fields
            if not subscription_id or not amount or not payment_date or not payment_method or not status:
                return jsonify({"error": "Missing required fields"}), 400

            # Create a new payment
            new_payment = Payment(
                subscription_id=subscription_id,
                amount=amount,
                payment_date=payment_date,
                payment_method=payment_method,
                status=status
            )
            db.session.add(new_payment)
            db.session.commit()

            return jsonify({"message": "Payment created successfully"}), 201

        except Exception as e:
            db.session.rollback()  # Rollback the session in case of an error
            return jsonify({"error": str(e)}), 500

    # Render a form for creating a payment (for HTML template use)
    if request.method == 'GET':
        return render_template('create_payment.html')
