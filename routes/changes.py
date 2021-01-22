import requests
from bs4 import BeautifulSoup
from flask_restful import Resource

from static import Static


class ChangesParser():
    def parse_changes(self, url):
        r = requests.get(url)
        html_content = r.text
        soup = BeautifulSoup(html_content, 'html.parser')
        tables = soup.findChildren('table')
        changes = []
        for table in tables:
            my_table = table
            rows = my_table.find_all('tr')
            for row in rows:
                cells = row.find_all('td')
                change = Static.change_template(cells)
                if change and change['dayofweek'] != "" and change['teacher'] != "Õpetaja":
                    changes.append(change)
                continue
        return changes


class Changes(Resource):
    def get(self):
        url = Static.changes_link()
        changes = ChangesParser().parse_changes(url)
        if changes:
            return {"data": changes}, 200
        return None, 204
