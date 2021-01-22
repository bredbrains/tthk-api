from flask import Flask, redirect
from flask_cors import CORS
from flask_restful import Api

from routes.changes import Changes
from routes.consultations import Consultations

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})


@app.route('/')
def index():
    return redirect('https://github.com/bredbrains/tthk-api', 302)


api = Api(app)
api.add_resource(Changes, '/changes')
api.add_resource(Consultations, '/consultations')

if __name__ == '__main__':
    app.run(threaded=True)
