from datetime import datetime

from extensions import db
from models.RolePermission import RolePermission


class Role(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)
    permissions = db.relationship('Permission', secondary=RolePermission, backref='roles')
    created_at = db.Column(db.DateTime, default=datetime.now())

    def __repr__(self):
        return f'<Role id={self.id}, name={self.name}>'
