from flask import Flask 
from flask_sqlalchemy import SQLAlchemy 


app = Flask(__name__)
app.config['SECRET_KEY'] = 'd8937da7edc9c7452ae99bdcaec96e88'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)

from flaskblog import routes