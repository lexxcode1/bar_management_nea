from datetime import datetime

from extensions import db


class Staff(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.Text())
    role_id = db.Column(db.Integer(), db.ForeignKey('role.id'))
    role = db.relationship('Role')
    created_bills = db.relationship('Bill')
    wage = db.Column(db.Float(), default=0.0)
    created_at = db.Column(db.DateTime(), default=datetime.now())
    updated_at = db.Column(db.DateTime(), default=datetime.now())

    def __repr__(self):
        return f'<Staff id={self.id}, name={self.name}, role_id={self.role_id}, wage={self.wage}>'
