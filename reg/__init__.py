from flask import Flask
from flask_sqlalchemy import SQLAlchemy




app = Flask(__name__)

app.config['SECRET_KEY'] = '8ea2a86e42689205dde0ba81f31138b6'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///reg_app.db'

db = SQLAlchemy(app)





from reg import routes