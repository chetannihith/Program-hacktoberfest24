from app import app
import unittest

class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client(self)

    def test_add(self):
        response = self.client.get('/add?a=2&b=2')
        self.assertIn(b'4', response.data)
        self.assertEqual(response.status_code, 200)

    def test_subtract(self):
        response = self.client.get('/sub?a=2&b=2')
        self.assertIn(b'0', response.data)
        self.assertEqual(response.status_code, 200)

    def test_multiply(self):
        response = self.client.get('/mult?a=20&b=2')
        self.assertIn(b'40', response.data)
        self.assertEqual(response.status_code, 200)

    def test_division(self):
        response = self.client.get('/div?a=2&b=2')
        self.assertIn(b'1', response.data)
        self.assertEqual(response.status_code, 200)

    def test_all_in_one(self):
        response = self.client.get('/math/add?a=2&b=2')
        self.assertIn(b'4', response.data)
        self.assertEqual(response.status_code, 200)

        response = self.client.get('/math/sub?a=2&b=2')
        self.assertIn(b'0', response.data)
        self.assertEqual(response.status_code, 200)

        response = self.client.get('/math/mult?a=20&b=2')
        self.assertIn(b'40', response.data)
        self.assertEqual(response.status_code, 200)

        response = self.client.get('/math/div?a=2&b=2')
        self.assertIn(b'1', response.data)
        self.assertEqual(response.status_code, 200)
