import requests
from bs4 import BeautifulSoup
from flask_restful import Resource, reqparse
from static import Static


def parse_groups(url):
    parsed_groups = []
    group_cell = 0
    get_request = requests.get(url)
    html_content = get_request.text
    soup = BeautifulSoup(html_content, 'html.parser')
    tbodies = soup.findChildren('tbody')
    for index, table in enumerate(tbodies):
        new_table = table
        rows = new_table.find_all('tr')
        for row in rows:
            cells = row.find_all('td')
            if cells[0].text.strip() != "Õppegrupp":
                group = Static.group_template(cells, index)
                parsed_groups.append(group)
    return parsed_groups

class Groups(Resource):
    def get(self):
        url = Static.changes_link()
        changes = parse_groups(url)
        if changes:
            return {"data": changes}, 200
        return None, 204