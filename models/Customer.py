from datetime import datetime

from extensions import db


class Customer(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(20), nullable=False)
    bills = db.relationship('Bill', backref='customer')
    vip = db.Column(db.Boolean(), default=False)
    created_at = db.Column(db.DateTime(), default=datetime.now())
    updated_at = db.Column(db.DateTime(), default=datetime.now())

    def __repr__(self):
        return f'<Customer id={self.id}, name="{self.name}", vip={self.vip}>'
