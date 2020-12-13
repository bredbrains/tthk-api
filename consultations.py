from flask_restful import Resource, reqparse
from bs4 import BeautifulSoup
import requests


class Consultations(Resource):
    def get(self):
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
        department_titles = ['general', 'transport', 'mechanics', 'energy', 'infotechnology', 'logistics', 'textile']
        consultations = []
        selected_department = args['department']
        weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
        if selected_department is not None:
            if selected_department < 0 or selected_department > 6:
                return None, 204
            url = requests.get(links[selected_department])
            html_content = url.text
            soup = BeautifulSoup(html_content, 'html.parser')
            tables = soup.findChildren('table')
            tablesbody = soup.findChildren('tbody')
            for table in tablesbody:
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
                    if selected_department == 6:
                        consultation = {
                            'teacher': cells[0].text.strip(),
                            'room': cells[2].text.strip(),
                            'times': []
                        }
                        start_cell = 3
                        end_cell = 8
                    x = 0
                    for i in range(start_cell, end_cell):
                        if cells[i].text.strip() != "" and x == 0:
                            consultation['times'].append({'weekday': weekdays[i - 2], 'time': cells[i].text.strip()})
                            x += 1
                        elif cells[i].text.strip() != "" and x == 1:
                            consultation['times'].append({'weekday': weekdays[i - 2], 'time': cells[i].text.strip()})
                        else:
                            pass
                    if consultation['times'] != [] and consultation['teacher'] != "Õpetaja":
                        consultations.append(consultation)
        else:
            for j in range(len(links)):
                url = requests.get(links[j])
                html_content = url.text
                soup = BeautifulSoup(html_content, 'html.parser')
                tables = soup.findChildren('table')
                tablesbody = soup.findChildren('tbody')
                for table in tablesbody:
                    new_table = table
                    rows = new_table.find_all('tr')
                    for row in rows:
                        cells = row.find_all('td')
                        consultation = {
                            'teacher': cells[0].text.strip(),
                            'room': cells[1].text.strip(),
                            'department': department_titles[j],
                            'times': []
                        }
                        start_cell = 2
                        end_cell = 7
                        if selected_department == 6:
                            consultation = {
                                'teacher': cells[0].text.strip(),
                                'room': cells[2].text.strip(),
                                'times': []
                            }
                            start_cell = 3
                            end_cell = 8
                        x = 0
                        for i in range(start_cell, end_cell):
                            if cells[i].text.strip() != "" and x == 0:
                                consultation['times'].append(
                                    {'weekday': weekdays[i - 2], 'time': cells[i].text.strip()})
                                x += 1
                            elif cells[i].text.strip() != "" and x == 1:
                                consultation['times'].append(
                                    {'weekday': weekdays[i - 2], 'time': cells[i].text.strip()})
                            else:
                                pass
                        if consultation['times'] != []  and consultation['teacher'] != "Õpetaja":
                            consultations.append(consultation)
        if consultations:
            return {'data': consultations}, 200
        return None, 204