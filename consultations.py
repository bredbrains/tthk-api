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
            changes = []


            for table in tablesbody:
                my_table = table
                rows = my_table.find_all('tr')
                for row in rows:
                    cells = row.find_all('td')
                    change = {
                        "teacher": cells[0].text.strip(),
                        "ruum": cells[1].text.strip(),
                        "Monday": cells[2].text.strip(),
                        "Tuesday": cells[3].text.strip(),
                        "Wednesday": cells[4].text.strip(),
                        "Thursday": cells[5].text.strip(),
                        "Friday": cells[6].text.strip(),
                    }
                    changes.append(change)

            if (changes != []):
                return {'data': changes}, 200
            else:
                return 204





