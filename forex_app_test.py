from unittest import TestCase
from app import app
import codecs


class RouteTests(TestCase):
    def setUp(self):
        self.app = app.test_client()
        app.config["TESTING"] = True
        
    def submit_form(self, data):
        return self.app.post('/convert', data=data)

    def test_home_route(self):
        res = self.app.get('/')
        self.assertEqual(res.status_code, 200)
        self.assertIn(b'Converting from:', res.data)
        self.assertIn(b'Converting to:', res.data)
        
    def test_convert_route(self):
        data ={
                'from_currency': 'USD',
                'to_currency': 'GBP',
                'amount': 100
            }
        res = self.submit_form(data)
        self.assertEqual(res.status_code, 200)
        
        #Check for flashed success message
        pound_symbol = codecs.encode('£', 'utf-8')
        self.assertIn(b'The result is:', res.data)
        self.assertIn(pound_symbol, res.data)
            
    def test_invalid_codes(self):
        data ={
                'from_currency': 'ZZZ',
                'to_currency': 'YYY',
                'amount': 100
            }  
        res = self.submit_form(data)
        self.assertEqual(res.status_code, 200)
        self.assertIn(b'Not a valid code: ZZZ', res.data)
        self.assertIn(b'Not a valid code: YYY', res.data)
                
    def test_invalid_amount(self):
        invalid_amounts = [
            (
                {'from_currency': 'USD', 'to_currency': 'GBP', 'amount': -10}, b'Not a valid amount.'
            ),
            (
                {'from_currency': 'USD', 'to_currency': 'GBP', 'amount': 0}, b'Not a valid amount.'
            ),
            (
                {'from_currency': 'USD', 'to_currency': 'GBP', 'amount': 'invalid'}, b'Invalid amount. Please enter a valid number.'
            ),
        ]
        
        for data, message in invalid_amounts:
            with self.subTest(data=data, message=message):
                res = self.submit_form(data)
                self.assertEqual(res.status_code, 200)
                self.assertIn(message, res.data)
        
   