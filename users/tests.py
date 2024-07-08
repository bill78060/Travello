from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User

class RegisterUserTestCase(TestCase):

    def setUp(self):
        self.client = Client()
        self.register_url = reverse('register')  # Replace 'register' with the name of your registration view

    def test_registration_with_missing_fields(self):
        response = self.client.post(self.register_url, {
            'username': '',
            'email': '',
            'first_name': '',
            'last_name': '',
            'password': '',
            'password2': ''
        })
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'All fields are required')

        response = self.client.post(self.register_url, {
            'username': 'testuser',
            'email': 'testuser@example.com',
            'first_name': '',
            'last_name': '',
            'password': 'password123',
            'password2': 'password123'
        })
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'All fields are required')

    def test_registration_with_all_fields(self):
        response = self.client.post(self.register_url, {
            'username': 'testuser',
            'email': 'testuser@example.com',
            'first_name': 'Test',
            'last_name': 'User',
            'password': 'password123',
            'password2': 'password123'
        })
        self.assertEqual(response.status_code, 302)  # Should redirect to success page
        self.assertRedirects(response, '/')
        self.assertTrue(User.objects.filter(username='testuser').exists())
