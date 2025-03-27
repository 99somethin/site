from django.test import TestCase
from django.urls import reverse
from article.models import Article
# Create your tests here.

class test_names(TestCase):
    def test_articles_names(self):
        response = self.client.get(reverse('all_articles'))
        self.assertEqual(response.status_code,200)


class ArticlesTest(TestCase):
    def setUp(self):
        Article.objects.create(name='new_article', body='something')

    def testUpdate(self):
        response = self.client.post(reverse(('current_article'), kwargs={'name': 'bob', 'body': 'new_body'}))
        self.assertEqual(response.status_code, 200)
