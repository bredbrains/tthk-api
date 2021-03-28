import random
import unittest
from unittest import TestCase

from app import app
import routes.consultations
from static import Static

links = Static.consultation_links()

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
