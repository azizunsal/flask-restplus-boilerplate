from typing import Tuple, Dict

from flask import request
from flask_restplus import Resource

from app.main.dto.CustomerDto import CustomerDto
from app.main.service.customer_service import get, get_all, create

api = CustomerDto.api
_customer = CustomerDto.customer

@api.route('/')
class CustomerList(Resource):
    @api.doc('list_of_the_customers')
    @api.marshal_list_with(_customer, envelope='data')
    def get(self):
        """
        List of the customers
        """
        return get_all()

    @api.expect(_customer, validate=True)
    @api.response(201, 'Customer successfully created.')
    @api.doc('Create a new customer')
    def post(self) -> Tuple[Dict[str, str], int]:
        """Creates a new customer"""
        data = request.json
        return create(data=data)


class Customer(Resource):
    @api.doc('get a customer')
    @api.marshal_with(_customer)
    def get(self, id):
        """ get a user with given id"""
        customer = get(id)
        if not customer:
            api.abort(404)
        else:
            return customer
