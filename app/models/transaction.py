from . import db
from datetime import datetime
class Transaction(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    transaction_type = db.Column(db.String(50), nullable=False)
    amount = db.Column(db.Float, nullable=False)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    sender_account_id = db.Column(db.Integer, db.ForeignKey('account.id'), nullable=False)
    receiver_account_id = db.Column(db.Integer, db.ForeignKey('account.id'), nullable=True)

    sender_account = db.relationship('Account', foreign_keys=[sender_account_id], backref=db.backref('sent_transactions', lazy=True))
    receiver_account = db.relationship('Account', foreign_keys=[receiver_account_id], backref=db.backref('received_transactions', lazy=True))

    def __repr__(self):
        return f'<Transaction {self.id}>'
