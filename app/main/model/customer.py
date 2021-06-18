from app.main import db
from app.main.model import audit


class Customer(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=True)
    audits = db.relationship('Audit', backref='customer', lazy=True)

    def __repr__(self):
        return f"<Customer '{self.name}'>"
