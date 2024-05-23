import unittest
from app import app

class BodegaTestCase(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_dashboard_access_without_login(self):
        response = self.app.get('/dashboard', follow_redirects=True)
        self.assertIn(b'Login', response.data)

    def test_products_access_without_login(self):
        response = self.app.get('/products', follow_redirects=True)
        self.assertIn(b'Login', response.data)

    def test_login_valid_credentials(self):
        response = self.app.post('/login', data=dict(username='valid_user', password='valid_password'), follow_redirects=True)
        self.assertIn(b'Dashboard', response.data)

    def test_dashboard_access_with_login(self):
        self.app.post('/login', data=dict(username='valid_user', password='valid_password'), follow_redirects=True)
        response = self.app.get('/dashboard')
        self.assertEqual(response.status_code, 200)

    def test_products_access_with_login(self):
        self.app.post('/login', data=dict(username='valid_user', password='valid_password'), follow_redirects=True)
        response = self.app.get('/products')
        self.assertEqual(response.status_code, 200)

    def test_location_access_with_login(self):
        self.app.post('/login', data=dict(username='valid_user', password='valid_password'), follow_redirects=True)
        response = self.app.get('/locations')
        self.assertEqual(response.status_code, 200)

    def test_product_movements_access_with_login(self):
        self.app.post('/login', data=dict(username='valid_user', password='valid_password'), follow_redirects=True)
        response = self.app.get('/product_movements')
        self.assertEqual(response.status_code, 200)

    def test_add_product_access_with_login(self):
        self.app.post('/login', data=dict(username='valid_user', password='valid_password'), follow_redirects=True)
        response = self.app.get('/add_product')
        self.assertEqual(response.status_code, 200)

    def test_add_location_access_with_login(self):
        self.app.post('/login', data=dict(username='valid_user', password='valid_password'), follow_redirects=True)
        response = self.app.get('/add_location')
        self.assertEqual(response.status_code, 200)

    def test_edit_product_access_with_login(self):
        self.app.post('/login', data=dict(username='valid_user', password='valid_password'), follow_redirects=True)
        response = self.app.get('/edit_product')
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()
