from enum import Enum

from app.main import db


class AuditTypes(Enum):
    FACE_DETECTION = 1
    FACE_EXTRACTION = 2
    FACE_VERIFICATION = 3


class Audit(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    time = db.Column(db.DateTime, nullable=False)
    customer_id = db.Column(db.Integer, db.ForeignKey('customer.id'), nullable=False)
    type = db.Column(db.Enum(AuditTypes), nullable=False)
