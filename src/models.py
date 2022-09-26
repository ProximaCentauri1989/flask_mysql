from src import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    payments = db.relationship('Payment', backref='user', lazy=True)

    def __repr__(self):
        return '<User {}>'.format(self.username)
    
    @property
    def as_json(self):
       """Return object data in easily serializable format"""
           
       return {
           'id' : self.id,
           'username': self.username,
           'email'  : self.email,
           'payments': [] if not self.payments else [item.as_json for item in self.payments]
       }
       
class Payment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    tx_id = db.Column(db.String(120), unique=True, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    
    @property
    def as_json(self):
       """Return object data in easily serializable format"""
       return {
           'tx_id' : self.tx_id,
           'user_id': self.user_id,
       }
