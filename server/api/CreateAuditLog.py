from flask import request, jsonify, render_template
from models import db, AuditLog  # Ensure AuditLog is imported

def create_audit_log():
    if request.method == 'POST':
        try:
            data = request.form if request.form else request.json
            table_name = data.get('table_name')
            record_id = data.get('record_id')
            action = data.get('action')
            user_id = data.get('user_id')
            details = data.get('details')

            # Validate required fields
            if not table_name or not record_id or not action:
                return jsonify({"error": "Missing required fields"}), 400

            # Create a new audit log
            new_audit_log = AuditLog(
                table_name=table_name,
                record_id=record_id,
                action=action,
                user_id=user_id,
                details=details
            )
            db.session.add(new_audit_log)
            db.session.commit()

            return jsonify({"message": "Audit log created successfully"}), 201

        except Exception as e:
            db.session.rollback()  # Rollback the session in case of an error
            return jsonify({"error": str(e)}), 500

    # Render a form for creating an audit log (for HTML template use)
    if request.method == 'GET':
        return render_template('create_audit_log.html')
