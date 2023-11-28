from datetime import datetime

from extensions import db
from models.BillItem import BillItem


class Bill(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    customer_id = db.Column(db.Integer(), db.ForeignKey('customer.id'))
    seating_id = db.Column(db.Integer(), db.ForeignKey('seating.id'))
    items = db.relationship('Item', secondary=BillItem, backref='bill')
    total = db.Column(db.Float(), default=0.0)
    covers = db.Column(db.Integer(), default=0)
    created_at = db.Column(db.DateTime(), default=datetime.now())
    created_by_staff_id = db.Column(db.Integer(), db.ForeignKey('staff.id'))
    updated_at = db.Column(db.DateTime(), default=datetime.now())

    def __repr__(self):
        return (f'<Bill id={self.id}, customer_id={self.customer_id}, table_id={self.table_id}, total={self.total}, '
                f'covers={self.covers}>',)
