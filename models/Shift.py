from datetime import datetime

from extensions import db


class Shift(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    staff_id = db.Column(db.Integer, db.ForeignKey('staff.id'))
    started_at = db.Column(db.DateTime, default=datetime.now())
    ended_at = db.Column(db.DateTime, default=datetime.now())
    break_length = db.Column(db.Integer, default=0)
    approved = db.Column(db.Boolean, default=False)
    approved_at = db.Column(db.DateTime)
    approval_id = db.Column(db.Integer, db.ForeignKey('approval.id'))
    created_at = db.Column(db.DateTime, default=datetime.now())
    updated_at = db.Column(db.DateTime, default=datetime.now())

    def __repr__(self):
        return f'<Shift length={self.ended_at - self.started_at}, break_length={self.break_length}, approved={self.approved}, approval_id={self.approval_id}>'
