import uuid
from typing import Dict, Tuple

from app.main.model.customer import Customer
from app.main import db


def get_all():
    return Customer.query.all()


def get(id):
    return Customer.query.filter_by(id=id).first()


def create(data: Dict[str, str]) -> Tuple[Dict[str, str], int]:
    # customer = Customer.query.filter_by()
    new_customer = Customer(
        name=data['name'],
        email=data['email']
    )

    save_changes(new_customer)


def save_changes(data: Customer) -> None:
    print(f"saving customer {data}")
    db.session.add(data)
    db.session.commit()
