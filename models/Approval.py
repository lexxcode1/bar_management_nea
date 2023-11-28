from datetime import datetime

from extensions import db


class Approval(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    staff_id = db.Column(db.Integer, db.ForeignKey('staff.id'))
    action_id = db.Column(db.Integer, db.ForeignKey('action.id'))
    created_at = db.Column(db.DateTime, default=datetime.now())
