from flask import request, jsonify, render_template
from models import db, Role  # Ensure Role is imported

def create_role():
    if request.method == 'POST':
        try:
            data = request.form if request.form else request.json
            role_name = data.get('role_name')

            # Validate required fields
            if not role_name:
                return jsonify({"error": "Missing required fields"}), 400

            # Check if role already exists
            if Role.query.filter_by(role_name=role_name).first():
                return jsonify({"error": "Role already exists"}), 400

            # Create a new role
            new_role = Role(role_name=role_name)
            db.session.add(new_role)
            db.session.commit()

            return jsonify({"message": "Role created successfully"}), 201

        except Exception as e:
            db.session.rollback()  # Rollback the session in case of an error
            return jsonify({"error": str(e)}), 500

    # Render a form for creating a role (for HTML template use)
    if request.method == 'GET':
        return render_template('create_role.html')
