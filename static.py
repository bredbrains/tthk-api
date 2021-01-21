class Static:
    @staticmethod
    def consultation_links():
        return [
            'https://www.tthk.ee/oppetoo/opetajate-konsultatsioonid/uldainete-konsultatsioonid/',
            'https://www.tthk.ee/oppetoo/opetajate-konsultatsioonid/transporditehnika-valdkonna-konsultatsioonid/',
            'https://www.tthk.ee/oppetoo/opetajate-konsultatsioonid/mehaanika-ja-metallitootluse-valdkonna'
            '-konsultatsioonid/',
            'https://www.tthk.ee/oppetoo/opetajate-konsultatsioonid/mehhatroonka-osakonna-konsultatsiooid/',
            'https://www.tthk.ee/infotehnoloogia-valdkonna-konsultatsioonid/',
            'https://www.tthk.ee/logistika-valdkonna-konsultatsioonid/',
            'https://www.tthk.ee/oppetoo/opetajate-konsultatsioonid/tekstiili-ja-kaubanduse-valdkonna-konsultatsioonid/'
        ]

    @staticmethod
    def changes_link():
        return 'http://www.tthk.ee/tunniplaani-muudatused/'

    @staticmethod
    def weekdays():
        return ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']

    @staticmethod
    def department_titles():
        return ['general', 'transport', 'mechanics', 'energy', 'infotechnology', 'logistics', 'textile']

    @staticmethod
    def consultation_template(cells, department):
        try:
            return {
                'teacher': cells[0].text.strip(),
                'room': cells[1].text.strip(),
                'email': None,
                'department': department,
                'times': []
            }
        except IndexError:
            return None

    @staticmethod
    def change_template(cells):
        try:
            return {
                "dayofweek": cells[0].text.strip(),
                "date": cells[1].text.strip(),
                "group": cells[2].text.strip(),
                "lessons": cells[3].text.strip(),
                "teacher": cells[4].text.strip(),
                "room": cells[5].text.strip()
            }
        except IndexError:
            return None
