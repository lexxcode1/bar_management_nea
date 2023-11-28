from datetime import datetime

from extensions import db


class Action(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    bill_id = db.Column(db.Integer, db.ForeignKey('bill.id'))
    staff_id = db.Column(db.Integer, db.ForeignKey('staff.id'))
    approved = db.Column(db.Boolean, default=False)
    approval_id = db.Column(db.Integer, db.ForeignKey('approval.id'))
    reason = db.Column(db.Text, nullable=True)
    type = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=datetime.now())
    updated_at = db.Column(db.DateTime, default=datetime.now())

    def __repr__(self):
        return f'<Action id={self.id}, bill_id={self.bill_id}, staff_id={self.staff_id}, approved={self.approved}, type={self.type}, reason={self.reason}>'
