from datetime import datetime

from extensions import db
from models.MenuItem import MenuItem


class Menu(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text, unique=True)
    items = db.relationship('Item', secondary=MenuItem, backref='items')
    active = db.Column(db.Boolean, default=True)
    full = db.Column(db.Boolean, default=False)
    created_at = db.Column(db.DateTime, default=datetime.now())
    updated_at = db.Column(db.DateTime, default=datetime.now())

    def __repr__(self):
        return f'<Menu id={self.id}, name={self.name}, active={self.active}, full={self.full}>'
