from flask_restful import Resource
from bs4 import BeautifulSoup
import requests


class Changes(Resource):
    def get(self):
        r = requests.get('http://www.tthk.ee/tunniplaani-muudatused/')
        html_content = r.text
        soup = BeautifulSoup(html_content, 'html.parser')
        tables = soup.findChildren('table')
        changes = []
        for table in tables:
            my_table = table
            rows = my_table.find_all('tr')
            for row in rows:
                cells = row.find_all('td')
                change = {
                    "dayofweek": cells[0].text.strip(),
                    "date": cells[1].text.strip(),
                    "group": cells[2].text.strip(),
                    "lessons": cells[3].text.strip(),
                    "teacher": cells[4].text.strip(),
                    "room": cells[5].text.strip()
                }
                if change['dayofweek'] != "" and change['teacher'] != "Õpetaja":
                    changes.append(change)
                else:
                    continue
        if changes:
            return changes, 200
        return 204