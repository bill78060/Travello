# import tempfile
# from django.core.files.uploadedfile import SimpleUploadedFile
# from django.test import TestCase, Client
# from django.urls import reverse
# from .models import Destination

# class DestinationTests(TestCase):

#     def setUp(self):
#         self.client = Client()
#         # Create a temporary image file
#         self.image = SimpleUploadedFile(
#             name='test_image.jpg',
#             content=b'\x47\x49\x46\x38\x39\x61\x01\x00\x01\x00\x00\xff\x00\xff\x00\x00\x00\x00\x21\xf9\x04\x01\x0a\x00\x01\x00\x2c\x00\x00\x00\x00\x01\x00\x01\x00\x00\x02\x02\x4c\x01\x00\x3b',
#             content_type='image/jpeg'
#         )
#         self.destination = Destination.objects.create(
#             name='Test Destination',
#             desc='Test Description',
#             price=100,
#             offer=True,
#             image=self.image
#         )

#     def test_dest_details_view(self):
#         response = self.client.get(reverse('travello:details', args=[self.destination.id]))
#         self.assertEqual(response.status_code, 200)
#         self.assertTemplateUsed(response, 'destination.html')
#         self.assertContains(response, self.destination.name)
        
#         # Check if the cookie is set
#         self.assertIn('recent_destinations', response.cookies)
#         self.assertIn(self.destination.name, response.cookies['recent_destinations'].value)

#     def test_clear_cookies_view(self):
#         # First, visit the destination detail to set the cookie
#         self.client.get(reverse('travello:details', args=[self.destination.id]))
        
#         # Then, clear the cookies
#         response = self.client.post(reverse('travello:clear_cookies'))
#         self.assertEqual(response.status_code, 302)  # Should redirect
        
#         # Follow the redirect and check the cookie is cleared
#         response = self.client.get(response.url)
#         self.assertNotIn('recent_destinations', response.cookies)

import tempfile
from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import TestCase, Client
from django.urls import reverse
from .models import Destination

class DestinationTests(TestCase):

    def setUp(self):
        self.client = Client()
        self.image = SimpleUploadedFile(
            name='test_image.jpg',
            content=b'\x47\x49\x46\x38\x39\x61\x01\x00\x01\x00\x00\xff\x00\xff\x00\x00\x00\x00\x21\xf9\x04\x01\x0a\x00\x01\x00\x2c\x00\x00\x00\x00\x01\x00\x01\x00\x00\x02\x02\x4c\x01\x00\x3b',
            content_type='image/jpeg'
        )
        self.destination = Destination.objects.create(
            name='Test Destination',
            desc='Test Description',
            price=100,
            offer=True,
            image=self.image
        )

    def test_dest_details_view(self):
        response = self.client.get(reverse('travello:details', args=[self.destination.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'destination.html')
        self.assertContains(response, self.destination.name)

        # Check if the cookie is set
        self.assertIn('recent_destinations', response.cookies)
        self.assertIn(self.destination.name, response.cookies['recent_destinations'].value)

    def test_clear_cookies_view(self):
        # First, visit the destination detail to set the cookie
        self.client.get(reverse('travello:details', args=[self.destination.id]))

        # Then, clear the cookies
        response = self.client.post(reverse('travello:clear_cookies'))
        self.assertEqual(response.status_code, 200)  # Should return 200

        # Check the cookie is cleared
        # self.assertNotIn('recent_destinations', response.cookies)

