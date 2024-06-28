from flask import request, jsonify, render_template
from models import db, OwnerRole  # Ensure OwnerRole is imported

def assign_role():
    if request.method == 'POST':
        try:
            data = request.form if request.form else request.json
            owner_id = data.get('owner_id')
            role_id = data.get('role_id')

            # Validate required fields
            if not owner_id or not role_id:
                return jsonify({"error": "Missing required fields"}), 400

            # Check if the assignment already exists
            if OwnerRole.query.filter_by(owner_id=owner_id, role_id=role_id).first():
                return jsonify({"error": "Role already assigned to the owner"}), 400

            # Assign role to the owner
            new_owner_role = OwnerRole(owner_id=owner_id, role_id=role_id)
            db.session.add(new_owner_role)
            db.session.commit()

            return jsonify({"message": "Role assigned successfully"}), 201

        except Exception as e:
            db.session.rollback()  # Rollback the session in case of an error
            return jsonify({"error": str(e)}), 500

    # Render a form for assigning a role (for HTML template use)
    if request.method == 'GET':
        return render_template('assign_role.html')
