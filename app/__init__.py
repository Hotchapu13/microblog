'''This file initializes the flask application 
    and organizes the application set'''

from flask import Flask # type: ignore
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

from app import routes