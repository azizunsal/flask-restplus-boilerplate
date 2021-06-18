from flask_restplus import Api
from flask import Blueprint

from app.main.controller.customer_controller import api as customer_ns

blueprint = Blueprint('api', __name__)
blueprint = Blueprint('api', __name__, url_prefix="/tee")

api = Api(
    blueprint,
    title='A Sample REST Application',
    version='0.0.1'
)

api.add_namespace(customer_ns)
