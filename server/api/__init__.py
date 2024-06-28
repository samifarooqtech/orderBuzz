from flask import Blueprint

api_bp = Blueprint('api', __name__)

from .CreateOwner import create_owner
from .CreateCust import create_customer
#from .CreateRestaurant import create_restaurant
from .CreateOrder import create_order
from .CreateSubscriptionPlan import create_subscription_plan
from .CreateSubscription import create_subscription
from .CreatePayment import create_payment
from .CreateRole import create_role
from .AssignRole import assign_role
from .CreateNotification import create_notification
from .CreateAuditLog import create_audit_log
'''from .UpdateOwner import update_owner
from .UpdateCustomer import update_customer
from .UpdateRestaurant import update_restaurant
from .ReadOwner import read_owner, read_owners
from .ReadCustomer import read_customer, read_customers
from .ReadRestaurant import read_restaurant, read_restaurants
from .DeleteOwner import delete_owner
from .DeleteCustomer import delete_customer
from .DeleteRestaurant import delete_restaurant
'''

api_bp.add_url_rule('/create-owner', view_func=create_owner, methods=['GET', 'POST'])
api_bp.add_url_rule('/create-customer', view_func=create_customer, methods=['GET', 'POST'])
#api_bp.add_url_rule('/create-restaurant', view_func=create_restaurant, methods=['GET', 'POST'])
api_bp.add_url_rule('/create-order', view_func=create_order, methods=['GET', 'POST'])
api_bp.add_url_rule('/create-subscription-plan', view_func=create_subscription_plan, methods=['GET', 'POST'])
api_bp.add_url_rule('/create-subscription', view_func=create_subscription, methods=['GET', 'POST'])
api_bp.add_url_rule('/create-payment', view_func=create_payment, methods=['GET', 'POST'])
api_bp.add_url_rule('/create-role', view_func=create_role, methods=['GET', 'POST'])
api_bp.add_url_rule('/assign-role', view_func=assign_role, methods=['GET', 'POST'])
api_bp.add_url_rule('/create-notification', view_func=create_notification, methods=['GET', 'POST'])
api_bp.add_url_rule('/create-audit-log', view_func=create_audit_log, methods=['GET', 'POST'])
'''api_bp.add_url_rule('/update-owner/<int:owner_id>', view_func=update_owner, methods=['PUT'])
api_bp.add_url_rule('/update-customer/<int:customer_id>', view_func=update_customer, methods=['PUT'])
api_bp.add_url_rule('/update-restaurant/<int:restaurant_id>', view_func=update_restaurant, methods=['PUT'])
api_bp.add_url_rule('/owner/<int:owner_id>', view_func=read_owner, methods=['GET'])
api_bp.add_url_rule('/owners', view_func=read_owners, methods=['GET'])
api_bp.add_url_rule('/customer/<int:customer_id>', view_func=read_customer, methods=['GET'])
api_bp.add_url_rule('/customers', view_func=read_customers, methods=['GET'])
api_bp.add_url_rule('/restaurant/<int:restaurant_id>', view_func=read_restaurant, methods=['GET'])
api_bp.add_url_rule('/restaurants', view_func=read_restaurants, methods=['GET'])
api_bp.add_url_rule('/delete-owner/<int:owner_id>', view_func=delete_owner, methods=['DELETE'])
api_bp.add_url_rule('/delete-customer/<int:customer_id>', view_func=delete_customer, methods=['DELETE'])
api_bp.add_url_rule('/delete-restaurant/<int:restaurant_id>', view_func=delete_restaurant, methods=['DELETE'])
'''