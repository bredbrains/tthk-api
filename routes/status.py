import requests
from flask_restful import Resource

links = [
    'https://www.tthk.ee/tunniplaani-muudatused/',
    'https://konsultatsioonid.thkit.ee/',
    'https://api.bredbrains.tech/consultations?department=0',
    'https://api.bredbrains.tech/changes',
    'https://api.bredbrains.tech/teachers',
    'https://api.bredbrains.tech/groups'
]

status_codes = {
    200: 'OK',
    204: 'No Content',
    400: 'Bad Request',
    404: 'Not Found',
    500: 'Internal Server Error'
}

class Status(Resource):
    def get(self):
        statuses = []
        for link in links:
            request = requests.get(link)
            statuses.append(request.status_code)
        return {'data': {
            'TTHK': statuses[0],
            'Consultations Web': statuses[1],
            'API Consultations': statuses[2],
            'API Changes': statuses[3],
            'API Teachers': statuses[4],
            'API Groups': statuses[5]
        }}, 200