from flask import Flask

from extensions import db
from models.Customer import Customer

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'

db.app = app
db.init_app(app)


@app.route("/")
def hello_world():
    return [str(x) for x in Customer.query.order_by(Customer.created_at).all()]
