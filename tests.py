import random
import unittest
from unittest import TestCase

from app import app
from routes.consultations import ConsultationsParser
from static import Static

links = Static.consultation_links()


class ConsultationsTest(TestCase):
    def setUp(self):
        self.parser = ConsultationsParser()

    def test_consultations_general(self):
        actual = parse_consultations(links[0], True, 'general')
        self.assertIsNotNone(actual)

    def test_consultations_transports(self):
        actual = parse_consultations(links[1], False, 'transport')
        self.assertIsNotNone(actual)

    def test_consultations_logistics(self):
        actual = parse_consultations(links[5], False, 'logistics')
        self.assertIsNotNone(actual)

    def test_consultations_ITcount(self):
        actual = parse_consultations(links[4], False, 'infotechnology')
        self.assertGreater(len(actual), 0)


class FlaskTests(TestCase):
    def setUp(self):
        self.client = app.test_client(self)

    def test_root(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 302)

    def test_changes(self):
        response = self.client.get('/changes')
        self.assertEqual(response.status_code, 200)

    def test_whole_consultations(self):
        response = self.client.get('/consultations')
        self.assertEqual(response.status_code, 200)

    def test_random_consultations(self):
        random_consultations = random.randint(0, 6)
        print(f'Randomly selected consultations: {random_consultations}')
        response = self.client.get('/consultations', json={'department': random_consultations})
        self.assertEqual(response.status_code, 200)

    def test_undefined_consultations(self):
        response = self.client.get('/consultations', json={'department': 7})
        self.assertEqual(response.status_code, 400)

    def test_undefined_route(self):
        response = self.client.get('/undefined')
        self.assertEqual(response.status_code, 404)


if __name__ == '__main__':
    unittest.main()
