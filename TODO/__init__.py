from flask import Flask 
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt


app = Flask(__name__) 
app.config['SECRET_KEY'] = 'ce93c0d66f7ea57ff4c6'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///Todo.db' # set the congif where you want to save the db 
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)

from Todo import routes 