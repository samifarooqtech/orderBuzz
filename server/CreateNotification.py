from flask import request, jsonify, render_template
from models import db, Notification  # Ensure Notification is imported

def create_notification():
    if request.method == 'POST':
        try:
            data = request.form if request.form else request.json
            customer_id = data.get('customer_id')
            message = data.get('message')

            # Validate required fields
            if not customer_id or not message:
                return jsonify({"error": "Missing required fields"}), 400

            # Create a new notification
            new_notification = Notification(
                customer_id=customer_id,
                message=message
            )
            db.session.add(new_notification)
            db.session.commit()

            return jsonify({"message": "Notification created successfully"}), 201

        except Exception as e:
            db.session.rollback()  # Rollback the session in case of an error
            return jsonify({"error": str(e)}), 500

    # Render a form for creating a notification (for HTML template use)
    if request.method == 'GET':
        return render_template('create_notification.html')
