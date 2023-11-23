from flask import Flask, request
from flask_cors import CORS, cross_origin
import json

app = Flask(__name__)
CORS(app)


@app.route("/users", methods=['GET'])
def user_list():
    users = request.get_json().get('users', None)
    data = json.load(open('variable/iou.json', 'r'))
    if users is not None:
        users.sort()
    return json.dumps({"data": data}), 200


@app.route("/add", methods=['POST'])
def add_user():
    user = request.get_json().get('users', None)
    data = {"name": f"{user}", "owes": {}, "owed_by": {}}
    with open('variable/iou.json', 'w') as file:
        json.dump(data, file)
    return json.dumps({"data": data}), 200


@app.route("/iou", methods=['POST'])
def add_iou():
    lender = request.get_json().get('lender', None)
    borrower = request.get_json().get('borrower', None)
    amount = request.get_json().get('amount', 0)
    data = json.load(open('variable/iou.json', 'r'))
    for x in data:
        if lender == x['name']:
            x['owes'] += {f"{lender}": amount}
        if borrower == x['name']:
            x['owed_by'] += {f"{borrower}": amount}
    with open('variable/iou.json', 'w') as file:
        json.dump(data, file)


if __name__ == '__main__':
    app.run(debug=True, port=5000)



