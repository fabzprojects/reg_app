from reg import db,app
from flask_login import UserMixin





class Register(db.Model, UserMixin):
    id=db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(80))
    password = db.Column(db.String(80))
  
    name = db.Column(db.String(200))
    address = db.Column(db.String(200))
    contact = db.Column(db.String(200))
   


