from flask_restful import Resource
from bs4 import BeautifulSoup
import requests


class Consultations(Resource):
    def get(self):
            url = requests.get('https://www.tthk.ee/oppetoo/opetajate-konsultatsioonid/uldainete-konsultatsioonid/')
            html_content = url.text
            soup = BeautifulSoup(html_content, 'html.parser')
            tables = soup.findChildren('table')
            tablesbody = soup.findChildren('tbody')
            consultations = []
            weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']


            for table in tablesbody:
                new_table = table
                rows = new_table.find_all('tr')
                for row in rows:
                    cells = row.find_all('td')
                    consultation = {
                        'teacher': cells[0].text.strip(),
                        'room': cells[1].text.strip(),
                        'times': {}

                    }
                    x = 0
                    for i in range(2, 7):
                        if cells[i].text.strip() != "" and x == 0:
                            consultation['times'].update({0: {'weekday': weekdays[i-2], 'time': cells[i].text.strip()}})
                            x += 1;
                        elif cells[i].text.strip() != "" and x == 1:
                            consultation['times'].update({1: {'weekday': weekdays[i-2], 'time': cells[i].text.strip()}})
                        else:
                            pass
                    if consultation['times'] != {} and consultation['teacher'] != "Õpetaja":
                        consultations.append(consultation)

            if (consultations != []):
                return {'data': consultations}, 200
            return 204





