from flask_restplus import Namespace, fields


class CustomerDto:
    api = Namespace('customer', description='Customer related operations')

    customer = api.model('customer', {
        'id': fields.Integer(required=False, description="Id"),
        'name': fields.String(required=True, description='Customer first name'),
        'email': fields.String(required=True, description='Customer e-mail address'),
    })
