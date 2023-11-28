from datetime import datetime

from extensions import db


class Seating(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    flagged = db.Column(db.Boolean, default=False)
    status = db.Column(db.Text, default='clear')
    covers = db.Column(db.Integer, default=0)
    bills = db.relationship('Bill', backref='seating')
    type = db.Column(db.Text, default='table')
    created_at = db.Column(db.DateTime, default=datetime.now)
    updated_at = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now())

    def __repr__(self):
        return f'<Seating id={self.id}, flagged={self.flagged}, status={self.status}, covers={self.covers}>'
