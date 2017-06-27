from django.core.urlresolvers import resolve
from django.test import TestCase, Client
from django.http import HttpRequest
from django.template.loader import render_to_string
from bookstore.models import Book, Category, Review
from bookstore.views import home, index, newbook
from django.contrib.auth.models import User 
from django.contrib.auth import authenticate, login, logout
from django.db.models import Count,Max,Avg
from django.utils import timezone
import re

class LoginAndRegisterTest(TestCase):

    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/')  
        self.assertEqual(found.func, index)  

    def remove_csrf(self,html_code):
        csrf_regex = r'<input[^>]+csrfmiddlewaretoken[^>]+>'
        return re.sub(csrf_regex,'',html_code)

    def test_login_page_returns_correct_html(self):
        request = HttpRequest()  
        response = index(request) 
        expected_html = render_to_string('bookstore/login.html')
        self.assertEqual(self.remove_csrf(response.content.decode()), expected_html)
         

    def test_register_has_to_work_properly(self):
        response = self.client.post('/register/') 
        self.assertEqual(response.templates[0].name, 'bookstore/register.html')       
        first_user = User.objects.create_user(username='kati',email='kati@mail.com',password='kati123')
        first_user.save()
        allusers = User.objects.all()
        self.assertEqual(allusers.count(), 1)

        second_user = User.objects.create_user(username='plakat',email='plakat@mail.com',password='plakat123')
        second_user.save()
        allusers = User.objects.all()
        self.assertEqual(allusers.count(), 2)

        first_user = allusers[0]
        second_user = allusers[1]
        self.assertEqual(first_user.username, 'kati')
        self.assertEqual(second_user.username, 'plakat')

    def test_login_has_to_work_properly(self):
        
        self.client = Client()
        response = self.client.get('/')
        self.assertEqual(response.templates[0].name, 'bookstore/login.html') 
        self.assertEqual(response.status_code, 200)
        #self.assertTrue('Log in' in response.content)
        login = self.client.login(username='kati', password='kati123')
        response = self.client.get('/kati/')
        self.assertTrue(response.status_code, 200) 
        #self.assertTrue(login)
        self.assertEqual(response.templates[0].name, 'bookstore/home.html') 

##### !! change class name !! #####
class AddNewBookTest(TestCase):

    def remove_csrf(self,html_code):
        csrf_regex = r'&lt;input[^&gt;]+csrfmiddlewaretoken[^&gt;]+&gt;'
        return re.sub(csrf_regex,'',html_code)

    def test_add_new_book_page_returns_correct_html(self):
        response = self.client.post('/kati/newbook/')
        request = HttpRequest()  
        found = resolve('/kati/newbook/')  
        self.assertEqual(found.func, newbook)
        self.assertEqual(response.templates[0].name, 'bookstore/newbook.html')  
        self.assertTrue(response.status_code, 200) 
        
        
    def test_add_book_and_review(self):
        num_cat = Category.objects.filter(owner='kati')
        self.assertEqual(num_cat.count(), 0)

        first_cat = Category(name='Novel',owner='kati')
        first_cat.save()

        num_cat = Category.objects.filter(owner='kati')
        self.assertEqual(num_cat.count(), 1)

        first_book = Book(title='The Thief of Baramos', author='Rabbit', owner='kati', category=num_cat[0])
        first_book.save()
        book = Book.objects.filter(owner='kati')
        self.assertEqual(book.count(), 1)

        second_book = Book(title='The Thief of Baramos vol2', author='Rabbit', owner='kati', category=num_cat[0])
        second_book.save()
        book = Book.objects.filter(owner='kati')
        self.assertEqual(book.count(), 2)

        
        first_review = Review(book=book[0],timestamp=timezone.now(),review_message='สนุกมาก', rating=4)
        first_review.save()
              
        avg = Book.objects.filter(id=book[0].id).update(avg_rating = Review.objects.filter(book=book[0]).aggregate(Avg('rating')).get('rating__avg', 0.00))
        update = Book.objects.filter(id=book[0].id).update(update_review = timezone.now())

        second_review = Review(book=book[1],timestamp=timezone.now(),review_message='สนุกมาก', rating=4)
        second_review.save()

        third_review = Review(book=book[1],timestamp=timezone.now(),review_message='สนุกมาก', rating=5)
        third_review.save()

        avg = Book.objects.filter(id=book[1].id).update(avg_rating = Review.objects.filter(book=book[1]).aggregate(Avg('rating')).get('rating__avg', 0.00))
        update = Book.objects.filter(id=book[1].id).update(update_review = timezone.now())


        num_review = Review.objects.all()
        self.assertEqual(num_review.count(),3)
        self.assertEqual(book[0].avg_rating,4)
        self.assertEqual(book[1].avg_rating,4.5)


        response = self.client.post('/kati/2/')
        self.assertEqual(response.templates[0].name, 'bookstore/display_title.html') 

class TemplatesAndRedirectsTest(TestCase):      
        def search_template_test(self):
            response = self.client.post('/kati/search/')
            self.assertEqual(response.templates[0].name, 'bookstore/category.html')
        def category_template_test(self):
            response = self.client.post('/kati/cat/Allbooks/')
            self.assertEqual(response.templates[0].name, 'bookstore/category.html')
        def about_template_test(self):
            response = self.client.post('/kati/about/')
            self.assertEqual(response.templates[0].name, 'bookstore/about.html')
        def logout_redirect_and_template_test(self):
            response = self.client.get('/kati/logout/') 
            self.assertRedirects(response, '/')
            self.assertEqual(response.templates[0].name, 'bookstore/login.html')
        
