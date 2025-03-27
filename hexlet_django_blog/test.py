from django.test import TestCase
from django.urls import reverse



class UsersTest(TestCase):
    def test_main_page(self):
        response = self.client.get(reverse('main_page'))
        self.assertEqual(response.status_code, 302)





    