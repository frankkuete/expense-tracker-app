from flask import Flask, request
from flask_restful import Api, Resource
from flasgger import Swagger
from pymongo import MongoClient
from dotenv import load_dotenv
import os

# load environment variables
load_dotenv()

mongo_uri = os.getenv("MONGODB_URI")

# create flask app

app = Flask(__name__)
api = Api(app)
swagger = Swagger(app)

client = MongoClient("mongodb://localhost:27017/")
db = client.get_database("accounts")
accounts = db.get_collection("accounts")

class Account(Resource):
    def get(self):
        """
        returns an account
        ----
        tags:
          - accounts
        responses:
          200:
            description: account returned
        """
        return { 'id': 123 }
    def post(self):
        """
        creates an account
        ----
        tags:
          - accounts
        parameters:
          - in: body
            name: account
            schema:
              type: object
              properties:
                name:
                  type: string
                balance:
                  type: number
        responses:
          201:
            description: account created
        """
        data = request.get_json()
        response = accounts.insert_one(data)
        if response.acknowledged:
            return { 'id': str(response.inserted_id) }
        else:
            return { 'error': 'account not created' }

api.add_resource(Account, '/accounts')

if __name__ == '__main__':
    app.run(port=5001, debug=True)