import unittest
from flask import Flask
from app import app

class FlaskAppTestCase(unittest.TestCase):

    def setUp(self):
        app.config['TESTING'] = True
        self.app = app.test_client()

    def tearDown(self):
        pass

    def test_hello_geek(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Hello from Flask & Docker', response.data)

    def test_time(self):
        response = self.app.get('/time')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'time', response.data)

if __name__ == '__main__':
    unittest.main()
