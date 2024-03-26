from flask import Flask
from flask_restful import Api, Resource
from flasgger import Swagger

app = Flask(__name__)
api = Api(app)
swagger = Swagger(app)

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

api.add_resource(Account, '/accounts')

if __name__ == '__main__':
    app.run(port=5001, debug=True)