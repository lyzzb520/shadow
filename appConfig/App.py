from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from appConfig import Config
app = Flask(__name__)
app.config.from_object(Config.Base)
db = SQLAlchemy(app)
