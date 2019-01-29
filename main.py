from flask import Flask, request
from flask_restful import Api, Resource
from linkedin_api import Linkedin

login = '****@****.com'
password = '******'

# Authenticate using any Linkedin account credentials
linkedin = Linkedin(login, password)
app = Flask(__name__)
api = Api(app)


class Profile(Resource):
    def get(self, nickname):
        return linkedin.get_profile(nickname)

api.add_resource(Profile, '/profile/<nickname>')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')