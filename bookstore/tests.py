from django.core.urlresolvers import resolve
from django.test import TestCase
from django.http import HttpRequest
from django.template.loader import render_to_string

from bookstore.views import home #1

class HomePageTest(TestCase):

    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/')  #2
        self.assertEqual(found.func, home)  #3
    
    def test_home_page_returns_correct_html(self):
        request = HttpRequest()  #1
        response = home(request)  #2
        expected_html = render_to_string('home.html')
        self.assertEqual(response.content.decode(), expected_html)
