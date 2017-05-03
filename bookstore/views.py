from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from django.http import HttpResponse
from django.template import loader
from .models import Book,Review,User
from django.db.models import Count,Max,Avg
import datetime


def home(request):
    num_books = Book.objects.aggregate(Max('id')).get('id__max', 0.00)
    latest_book = Book.objects.all().order_by('-id')[:5]
    latest_review = Review.objects.all().order_by('-id')[:5]
    top5book = Book.objects.all().order_by('-avg_rating')[:5]
        
    template = loader.get_template('bookstore/home.html')
    context = {
        'latest_book' : latest_book,
        'num_books' : num_books,
        'latest_review' : latest_review,
        'top_five_rating' : top5book,
        
    }
    return HttpResponse(template.render(context, request))
    
def category(request,cat):
    if cat == 'Allbooks':
        book = Book.objects.all().order_by('title')
        
    else:
        book = Book.objects.filter(category=cat).order_by('title')

        
    template = loader.get_template('bookstore/category.html')
    context = {
       'book' : book,
       'cat' : cat,
    }
    return HttpResponse(template.render(context, request))

def display_title(request,book_id):
    book_name = get_object_or_404(Book, pk=book_id)
    book_review = Review.objects.filter(book=book_name)
  
    
    template = loader.get_template('bookstore/display_title.html')
    context = {
        'book_name' : book_name,
        'book_review' : book_review,
       
    }
    return HttpResponse(template.render(context, request))

def reserve(request,book_id):
    book = Book.objects.filter(id=book_id).update(available = 'False')
    template = loader.get_template('bookstore/reserve.html')
    context = {
        
    }
    return HttpResponse(template.render(context, request))

def review(request,book_id):
    book_name = Book.objects.filter(id=book_id)
    new_review_message = request.POST.get('review_message')
    new_rating = request.POST.get('rating')
    book_review = Review.objects.filter(book=book_name)
    message=""
    
    if (new_review_message != "") and (new_rating != ""):
        
        for a in book_name: 

            new_review = Review(book=a,timestamp=timezone.now(),review_message=new_review_message,rating=new_rating)
            new_review.save()

            avg = Book.objects.filter(id=book_id).update(avg_rating = Review.objects.filter(book=book_name).aggregate(Avg('rating')).get('rating__avg', 0.00))
          
        message = "your review successful!!"
        
    else:
        message = "your review unsuccessful."

    context = {
        'message' : message,
    }
    template = loader.get_template('bookstore/review.html')
    return HttpResponse(template.render(context, request))

 
def login(request):
    
    return render(request,"bookstore/login.html",{})


def checklogin(request):
    check=""
    username_login = request.POST['uname']
    password_login = request.POST['password']

    user = User.objects.filter(username=username_login,password=password_login)
    
    for u in user:
        
        if u != "":
            check = u

    if check !="":
        return HttpResponseRedirect('/bookstore/home/')
            
    else:
        template = loader.get_template('bookstore/loginfailed.html')
        context = {
        
        }
        return HttpResponse(template.render(context, request))

def display_allreviews(request):
    allreviews = latest_review = Review.objects.all().order_by('-id')
    template = loader.get_template('bookstore/allreviews.html')
    context = {
        'allreviews' : allreviews,
    }
    return HttpResponse(template.render(context, request))

def search(request):
   
    search_query = request.GET['search']
    book = Book.objects.filter(title__contains=search_query)
    template = loader.get_template('bookstore/category.html')
    context = {
        'book' : book,
    }
    return HttpResponse(template.render(context, request))
    #return HttpResponseRedirect(reverse('bookstore', args=(idbook,)))

