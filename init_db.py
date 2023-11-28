from app import app
from extensions import db

# noinspection PyUnresolvedReferences
from models import *

with app.app_context():
    db.drop_all()
    db.create_all()
