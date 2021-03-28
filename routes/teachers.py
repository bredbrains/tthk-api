import requests
from bs4 import BeautifulSoup
from flask_restful import Resource, reqparse

from static import Static


def parse_teachers(url):
    parsed_teachers = []
    teacher_cell = 0
    get_request = requests.get(url)
    html_content = get_request.text
    soup = BeautifulSoup(html_content, 'html.parser')
    tbodies = soup.findChildren('tbody')
    for table in tbodies:
        new_table = table
        rows = new_table.find_all('tr')
        for row in rows:
            cells = row.find_all('td')
            teacher = cells[teacher_cell].text.strip()
            if len(teacher.split()) == 2 and teacher != "Õpetaja":
                parsed_teachers.append(teacher)
    return parsed_teachers


class Teachers(Resource):
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('department', type=int)
        args = parser.parse_args()
        links = Static.consultation_links()
        teachers = list()
        department = args['department']
        if department is not None:
            department = args['department']
            if 0 <= department <= 6:
                teachers = parse_teachers(links[department])
            else:
                return None, 400
        else:
            for department, link in enumerate(links):
                teachers += parse_teachers(links[department])
        if teachers:
            return {'data': teachers}, 200
        return None, 204