from flask import Flask, request
from flask_restful import Api
from flask_cors import CORS
from changes import Changes
from consultations import Consultations

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})

@app.route('/')
def index():
    return "Index!"

api = Api(app)
api.add_resource(Changes, '/changes')
api.add_resource(Consultations, '/consultations')

if __name__ == '__main__':
    app.run(threaded=True)
