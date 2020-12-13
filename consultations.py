from flask_restful import Resource, reqparse
from bs4 import BeautifulSoup
import requests

weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
department_titles = ['general', 'transport', 'mechanics', 'energy', 'infotechnology', 'logistics', 'textile']


class ConsultationsParser():
    def parse_consultations(self, url, is_textile):
        parsed_consultations = []
        get_request = requests.get(url)
        html_content = get_request.text
        soup = BeautifulSoup(html_content, 'html.parser')
        tablesbodies = soup.findChildren('tbody')
        print(url)
        for table in tablesbodies:
            new_table = table
            rows = new_table.find_all('tr')
            for row in rows:
                cells = row.find_all('td')
                consultation = {
                    'teacher': cells[0].text.strip(),
                    'room': cells[1].text.strip(),
                    'times': []
                }
                start_cell = 2
                end_cell = 7
                if is_textile:
                    consultation = {
                        'teacher': cells[0].text.strip(),
                        'room': cells[2].text.strip(),
                        'times': []
                    }
                    start_cell = 3
                    end_cell = 7
                for i in range(start_cell, end_cell):
                    if cells[i].text.strip() != "":
                        consultation['times'].append({'weekday': weekdays[i - 2], 'time': cells[i].text.strip()})
                if consultation['times'] != [] and consultation['teacher'] != "Õpetaja":
                    parsed_consultations.append(consultation)
        return parsed_consultations


class Consultations(Resource):
    def get(self):
        consultation_parser = ConsultationsParser()
        parser = reqparse.RequestParser()
        parser.add_argument('department', type=int)
        args = parser.parse_args()
        links = [
            'https://www.tthk.ee/oppetoo/opetajate-konsultatsioonid/uldainete-konsultatsioonid/',
            'https://www.tthk.ee/oppetoo/opetajate-konsultatsioonid/transporditehnika-valdkonna-konsultatsioonid/',
            'https://www.tthk.ee/oppetoo/opetajate-konsultatsioonid/mehaanika-ja-metallitootluse-valdkonna-konsultatsioonid/',
            'https://www.tthk.ee/oppetoo/opetajate-konsultatsioonid/mehhatroonka-osakonna-konsultatsiooid/',
            'https://www.tthk.ee/infotehnoloogia-valdkonna-konsultatsioonid/',
            'https://www.tthk.ee/logistika-valdkonna-konsultatsioonid/',
            'https://www.tthk.ee/oppetoo/opetajate-konsultatsioonid/tekstiili-ja-kaubanduse-valdkonna-konsultatsioonid/'
        ]
        consultations = []
        selected_department = args['department']
        if selected_department is not None:
            consultations = []
            selected_department = args['department']
            if selected_department == 6:
                consultations.append(consultation_parser.parse_consultations(links[selected_department], True))
            elif 0 <= selected_department <= 5:
                consultations.append(consultation_parser.parse_consultations(links[selected_department], False))
            else:
                pass
        else:
            for i, link in enumerate(links):
                if i == 6:
                    consultations.append(consultation_parser.parse_consultations(link, True))
                else:
                    consultations.append(consultation_parser.parse_consultations(link, False))
        if consultations:
            return {'data': consultations}, 200
        return None, 204
