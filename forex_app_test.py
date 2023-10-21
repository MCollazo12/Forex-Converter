from unittest import TestCase
from app import app


class RouteTests(TestCase):
    def setUp(self):
        self.app = app.test_client()
        app.config["TESTING"] = True

    def test_home_route(self):
        res = self.app.get('/')
            
        self.assertEqual(res.status_code, 200)
        self.assertIn(b'Converting from:', res.data)