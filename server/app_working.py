from flask import Flask
from flask_cors import CORS
from config import Config
from models import db
from flask_migrate import Migrate
from CreateOwner import create_owner
from CreateCust import create_customer  # Ensure correct import
from CreateOrder import create_order  # Import create_order
from CreateSubscriptionPlan import create_subscription_plan  # Import create_subscription_plan
from CreateSubscription import create_subscription  # Import create_subscription
from CreatePayment import create_payment  # Import create_payment
from CreateRole import create_role  # Import create_role
from AssignRole import assign_role  # Import assign_role
from CreateNotification import create_notification  # Import create_notification
from CreateAuditLog import create_audit_log  # Import create_audit_log

app = Flask(__name__)
app.config.from_object(Config)

CORS(app)  # Allow CORS for all routes (suitable for development)

db.init_app(app)  # Initialize database with the app
migrate = Migrate(app, db)  # Initialize Flask-Migrate

@app.route('/create-user', methods=['GET', 'POST'])
def create_user():
    return create_customer()

@app.route('/create-owner', methods=['GET', 'POST'])
def create_owner_route():
    return create_owner()

@app.route('/create-order', methods=['GET', 'POST'])
def create_order_route():
    return create_order()

@app.route('/create-subscription-plan', methods=['GET', 'POST'])
def create_subscription_plan_route():
    return create_subscription_plan()

@app.route('/create-subscription', methods=['GET', 'POST'])
def create_subscription_route():
    return create_subscription()

@app.route('/create-payment', methods=['GET', 'POST'])
def create_payment_route():
    return create_payment()

@app.route('/create-role', methods=['GET', 'POST'])
def create_role_route():
    return create_role()

@app.route('/assign-role', methods=['GET', 'POST'])
def assign_role_route():
    return assign_role()

@app.route('/create-notification', methods=['GET', 'POST'])
def create_notification_route():
    return create_notification()

@app.route('/create-audit-log', methods=['GET', 'POST'])
def create_audit_log_route():
    return create_audit_log()

if __name__ == '__main__':
    app.run(debug=True)
