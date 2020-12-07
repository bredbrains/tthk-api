from flask import Flask
from flask_restful import Api
from changes import Changes
from consultations import Consultations

app = Flask(__name__)
app.config.fromenvvar('ENV')
app.config.fromenvvar('SERVER_NAME')
app.config.fromenvvar('TESTING')
api = Api(app)

api.add_resource(Changes, '/changes')
api.add_resource(Consultations, '/consultations')

if __name__ == '__main__':
    app.run()