from flask import request, jsonify, render_template
from models import db, Subscription  # Ensure Subscription is imported

def create_subscription():
    if request.method == 'POST':
        try:
            data = request.form if request.form else request.json
            owner_id = data.get('owner_id')
            plan_id = data.get('plan_id')
            start_date = data.get('start_date')
            end_date = data.get('end_date')
            status = data.get('status')

            # Validate required fields
            if not owner_id or not plan_id or not start_date or not end_date or not status:
                return jsonify({"error": "Missing required fields"}), 400

            # Create a new subscription
            new_subscription = Subscription(
                owner_id=owner_id,
                plan_id=plan_id,
                start_date=start_date,
                end_date=end_date,
                status=status
            )
            db.session.add(new_subscription)
            db.session.commit()

            return jsonify({"message": "Subscription created successfully"}), 201

        except Exception as e:
            db.session.rollback()  # Rollback the session in case of an error
            return jsonify({"error": str(e)}), 500

    # Render a form for creating a subscription (for HTML template use)
    if request.method == 'GET':
        return render_template('create_subscription.html')
