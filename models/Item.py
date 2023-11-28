from datetime import datetime

from extensions import db


class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text, unique=True)
    purchase_price = db.Column(db.Float, default=0.0)
    selling_price = db.Column(db.Float, default=0.0)
    department = db.Column(db.Text)
    vat = db.Column(db.Float, default=20.0)
    quantity = db.Column(db.Integer, default=0)
    individual_volume = db.Column(db.Integer, default=0)
    total_volume = db.Column(db.Integer, default=0)
    created_at = db.Column(db.DateTime, default=datetime.now())
    updated_at = db.Column(db.DateTime, default=datetime.now())

    def __repr__(self):
        return f'<Item id={self.id}, name={self.name}, purchase_price={self.purchase_price}, selling_price={self.selling_price},... quantitiy={self.quantity}, vat={self.vat}>'
