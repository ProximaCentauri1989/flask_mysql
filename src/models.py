from src import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))

    def __repr__(self):
        return '<User {}>'.format(self.username)
    
    @property
    def as_json(self):
       """Return object data in easily serializable format"""
       return {
           'id'         : self.id,
           'username': self.username,
           'email'  : self.email,
       }
