import requests
from bs4 import BeautifulSoup
from flask_restful import Resource, reqparse

from static import Static

weekdays = Static.weekdays()
department_titles = Static.department_titles()


class ConsultationsParser():
    def parse_consultations(self, url, contains_email, department):
        parsed_consultations = []
        get_request = requests.get(url)
        html_content = get_request.text
        soup = BeautifulSoup(html_content, 'html.parser')
        tbodies = soup.findChildren('tbody')
        for table in tbodies:
            new_table = table
            rows = new_table.find_all('tr')
            for row in rows:
                cells = row.find_all('td')
                consultation = Static.consultation_template(cells, department)
                start_cell = 2
                end_cell = 7
                if contains_email:
                    consultation = Static.consultation_template(cells, department)
                    if '@' not in cells[1].text.strip():
                        consultation['email'] = cells[2].text.strip()
                        consultation['room'] = cells[1].text.strip()
                    else:
                        consultation['email'] = cells[1].text.strip()
                        consultation['room'] = cells[2].text.strip()
                    start_cell = 3
                    end_cell = 8
                for i in range(start_cell, end_cell):
                    if cells[i].text.strip() != "":
                        consultation['times'].append(
                            {'weekday': weekdays[i - start_cell], 'time': cells[i].text.strip()})
                if consultation and consultation['teacher'] != "Õpetaja" and consultation['times'] != []:
                    parsed_consultations.append(consultation)
        return parsed_consultations


class Consultations(Resource):
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('department', type=int)
        args = parser.parse_args()
        links = Static.consultation_links()
        consultations = []
        department = args['department']
        if department is not None:
            consultations = []
            department = args['department']
            if department == 0 or department == 6:
                consultations.append = ConsultationsParser.parse_consultations(links[department], True,
                                                                               department_titles[department])
            elif 0 < department <= 5:
                consultations = ConsultationsParser.parse_consultations(links[department], False,
                                                                        department_titles[department])
            else:
                pass
        else:
            for department, link in enumerate(links):
                if department == 0 or department == 6:
                    consultations += ConsultationsParser.parse_consultations(link, True, department_titles[department])
                else:
                    consultations += ConsultationsParser.parse_consultations(link, False, department_titles[department])
        if consultations:
            return {'data': consultations}, 200
        return None, 204
