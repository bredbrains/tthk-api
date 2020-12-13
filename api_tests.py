import unittest
from consultations import ConsultationsParser
links = ['https://www.tthk.ee/oppetoo/opetajate-konsultatsioonid/uldainete-konsultatsioonid/',
        'https://www.tthk.ee/oppetoo/opetajate-konsultatsioonid/transporditehnika-valdkonna-konsultatsioonid/',
        'https://www.tthk.ee/oppetoo/opetajate-konsultatsioonid/mehaanika-ja-metallitootluse-valdkonna-konsultatsioonid/',
        'https://www.tthk.ee/oppetoo/opetajate-konsultatsioonid/mehhatroonka-osakonna-konsultatsiooid/',
        'https://www.tthk.ee/infotehnoloogia-valdkonna-konsultatsioonid/',
        'https://www.tthk.ee/logistika-valdkonna-konsultatsioonid/',
        'https://www.tthk.ee/oppetoo/opetajate-konsultatsioonid/tekstiili-ja-kaubanduse-valdkonna-konsultatsioonid/']

class ConsultationsTest(unittest.TestCase):
    def test_consultations_general(self):
        actual = ConsultationsParser.parse_consultations(self, links[0], False, 'general')
        self.assertIsNotNone(actual)
    def test_consultations_transports(self):
        actual = ConsultationsParser.parse_consultations(self, links[1], False, 'transport')
        self.assertIsNotNone(actual)
    def test_consultations_logistics(self):
        actual = ConsultationsParser.parse_consultations(self, links[5], False, 'logistics')
        self.assertIsNotNone(actual)
    def test_consultations_ITcount(self):
        actual = ConsultationsParser.parse_consultations(self, links[4], False, 'infotechnology')
        self.assertGreater(len(actual), 0)

if __name__ == '__main__':
    unittest.main()
