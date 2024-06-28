from flask import request, jsonify, render_template
from models import db, SubscriptionPlan  # Ensure SubscriptionPlan is imported

def create_subscription_plan():
    if request.method == 'POST':
        try:
            data = request.form if request.form else request.json
            name = data.get('name')
            description = data.get('description')
            price = data.get('price')
            features = data.get('features')

            # Validate required fields
            if not name or not price:
                return jsonify({"error": "Missing required fields"}), 400

            # Create a new subscription plan
            new_plan = SubscriptionPlan(
                name=name,
                description=description,
                price=price,
                features=features
            )
            db.session.add(new_plan)
            db.session.commit()

            return jsonify({"message": "Subscription plan created successfully"}), 201

        except Exception as e:
            db.session.rollback()  # Rollback the session in case of an error
            return jsonify({"error": str(e)}), 500

    # Render a form for creating a subscription plan (for HTML template use)
    if request.method == 'GET':
        return render_template('create_subscription_plan.html')
