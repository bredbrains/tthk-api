import unittest

from consultations import ConsultationsParser
from static import Static

links = Static.consultation_links()


class ConsultationsTest(unittest.TestCase):
    def test_consultations_general(self):
        actual = ConsultationsParser.parse_consultations(links[0], True, 'general')
        self.assertIsNotNone(actual)

    def test_consultations_transports(self):
        actual = ConsultationsParser.parse_consultations(links[1], False, 'transport')
        self.assertIsNotNone(actual)

    def test_consultations_logistics(self):
        actual = ConsultationsParser.parse_consultations(links[5], False, 'logistics')
        self.assertIsNotNone(actual)

    def test_consultations_ITcount(self):
        actual = ConsultationsParser.parse_consultations(links[4], False, 'infotechnology')
        self.assertGreater(len(actual), 0)


if __name__ == '__main__':
    unittest.main()
