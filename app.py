from flask import Flask, redirect
from flask_cors import CORS
from flask_restful import Api

from routes.changes import Changes
from routes.consultations import Consultations
from routes.teachers import Teachers
from routes.groups import Groups
from routes.status import Status

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})


@app.route('/')
def index():
    return redirect('https://github.com/bredbrains/tthk-api', 302)


api = Api(app)
api.add_resource(Changes, '/changes')
api.add_resource(Consultations, '/consultations')
api.add_resource(Teachers, '/teachers')
api.add_resource(Groups, '/groups')
api.add_resource(Status, '/status')

if __name__ == '__main__':
    app.run(threaded=True, port=8000, host='0.0.0.0')
