import json
import requests
from os import getenv
from venmo_api import Client
from dotenv import load_dotenv

load_dotenv()
ACCESS_TOKEN = getenv('VENMO_ACCESS_TOKEN')


def main(event, context):
    venmo = Client(access_token=ACCESS_TOKEN)

    # Get the SHPE UTD user account -> we can just just remove this and hardcore it for the get_user_transaction tbh
    users = venmo.user.search_for_users(query="SHPE-UTD")

    transaction_list = venmo.user.get_user_transactions(users[0].id, limit=1)
    ret = transaction_list[0]
    for transaction in transaction_list:
        # We would parse this later on for the code they're supposed to input
        print(transaction)
        print(transaction.note)

    # PoC for getting comments - the venmo-api library doesn't support that rn
    response = requests.get("https://api.venmo.com/v1/stories/3202788592531276254",
                            headers={"User-Agent": "Venmo/7.44.0 (iPhone; iOS 13.0; Scale/2.0)",
                                     "Authorization": f"Bearer {ACCESS_TOKEN}"})

    body = {
        "transaction": ret.note,
        "comments": response.json()
    }

    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }

    return response

    # # Use this code if you don't use the http event with the LAMBDA-PROXY
    # # integration
    # """
    # return {
    #     "message": "Go Serverless v1.0! Your function executed successfully!",
    #     "event": event
    # }
    # """


if __name__ == "__main__":
    main('', '')
