from flask import Flask
from flask_restful import Api
from models import PaymentResource, PaymentStatusResource


def create_app():
    app = Flask(__name__)
    api = Api(app)


    api.add_resource(PaymentResource, "/api/v1/payments")
    api.add_resource(PaymentStatusResource, "/api/v1/payments/<string:payment_id>")

    return app