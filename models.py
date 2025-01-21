from flask_restful import Resource, reqparse
import uuid
import requests
from dotenv import load_dotenv
import os

load_dotenv()

API_KEY = os.getenv("API_KEY")

payments = {}

class PaymentResource(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument("customer_name", type=str, required=True, help="Customer name is required")
        parser.add_argument("customer_email", type=str, required=True, help="Customer email is required")
        parser.add_argument("amount", type=float, required=True, help="Payment amount is required")
        args = parser.parse_args()

        payment_id = f"PAY-{uuid.uuid4().hex[:6].upper()}"

        paystack_data = {
            "email": args["customer_email"],
            "amount": int(args["amount"] * 100),
            "reference": payment_id
        }

        headers = {
            "Authorization": f"Bearer {API_KEY}",
            "Content-Type": "application/json"
        }

        response = requests.post("https://api.paystack.co/transaction/initialize", json=paystack_data, headers=headers)

        if response.status_code == 200:
            response_data = response.json()
            payment_url = response_data["data"]["authorization_url"]

            payment = {
                "id": payment_id,
                "customer_name": args["customer_name"],
                "customer_email": args["customer_email"],
                "amount": args["amount"],
                "status": "pending",
                "payment_url": payment_url
            }

            payments[payment_id] = payment

            return {
                "payment": payment, 
                "status": "success",
                "message": "Payment initiated successfully"
            }, 201
        
        return {
            "status": "error",
            "message": response.json().get("message", "An error occurred while processing the payment")
        }, response.status_code
    


class PaymentStatusResource(Resource):
    def get(self, payment_id):
        payment = payments.get(payment_id)

        if payment:
            headers = {
                "Authorization": f"Bearer {API_KEY}"
            }
            response = requests.get(f"https://api.paystack.co/transaction/verify/{payment_id}", headers=headers)

            if response.status_code == 200:
                response_data = response.json()
                payment_status = response_data["data"]["status"]

                payment["status"] = payment_status

                return {
                "payment": payment,
                "status": "success",
                "message": "Payment details retrieved successfully"
            }, 200

            return {
                "status": "error",
                "message": response.json().get("message", "An error occurred while processing the payment")
            }, response.status_code
        
        return {
                "status": "error",
                "message": "Payment not found"
            }, 404