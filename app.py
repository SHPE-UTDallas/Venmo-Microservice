from flask import Flask, jsonify, request
from dotenv import load_dotenv
from venmo_api import Client
from os import getenv

load_dotenv()
ACCESS_TOKEN = getenv('VENMO_ACCESS_TOKEN')

app = Flask(__name__)
venmo = Client(access_token=ACCESS_TOKEN)


# Example of how to integrate with venmo api and use flask
@app.route("/createToken", methods=["POST"])
def create_token():
    user_id = request.json['userId']
    user = venmo.user.search_for_users(query=user_id)[0]
    print(user)
    transactions = venmo.user.get_user_transactions(user=user)
    print(transactions)
    return jsonify({
        'lastTransactionNote': transactions[0].note
    })


@app.route('/associateVenmoUsernameWithUser', methods=["POST"])
def associate_venmo_username_with_user():
    user_id = request.json.get('userId')
    venmo_username = request.json.get('venmoUsername')
    return jsonify({
        'userId': user_id,
        'venmo_username': venmo_username
    })


@app.route("/verifyPaymentStatus/<string:user_id>", methods=["GET"])
def verify_payment_status(user_id):
    return jsonify({
        'userId': user_id
    })


if __name__ == "__main__":
    app.run()
