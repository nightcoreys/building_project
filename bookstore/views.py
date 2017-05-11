from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from django.http import HttpResponse
from django.template import loader
from .models import Book,Review
from django.db.models import Count,Max,Avg
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.utils.datastructures import MultiValueDictKeyError
import datetime


def home(request):
    num_books = Book.objects.all().count()
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
    book_review = Review.objects.filter(book=book_name).order_by('-timestamp')[:5]
    image = Book.objects.filter(pk=book_id)
  
    
    template = loader.get_template('bookstore/display_title.html')
    context = {
        'book_name' : book_name,
        'book_review' : book_review,
        'image' : image,
    }
    return HttpResponse(template.render(context, request))


def review(request,book_id):
    book_name = Book.objects.filter(id=book_id)
    new_review_message = request.POST.get('review_message')
    new_rating = request.POST.get('rating')
    book_review = Review.objects.filter(book=book_name)
    message=""
    
    if (new_review_message != None) and (new_rating != None):
        
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

 

def display_allreviews(request):
    allreviews = latest_review = Review.objects.all().order_by('-id')
    template = loader.get_template('bookstore/allreviews.html')
    context = {
        'allreviews' : allreviews,
    }
    return HttpResponse(template.render(context, request))

def search(request):
    if 'tora' in request.GET:
        tora = request.GET['tora']
        search_query = request.GET['search']
        if tora == "title":

        
           book = Book.objects.filter(title__contains=search_query)
        elif tora =="author":
           book = Book.objects.filter(author__contains=search_query)
    else:
       book = None
    template = loader.get_template('bookstore/category.html')
    context = {
        'book' : book,
    }
    return HttpResponse(template.render(context, request))

def about(request):
    template = loader.get_template('bookstore/about.html')
    return HttpResponse(template.render({}, request))

def newbook(request):
    template = loader.get_template('bookstore/newbook.html')
    return HttpResponse(template.render({}, request))
    
def addnewbook(request):
    messaage=""
    try:
        if request.method == 'POST' and request.FILES['myfile']:
            new_title = request.POST.get('title')
            new_author = request.POST.get('author')
            new_cat = request.POST.get('cat')
            myfile = request.FILES['myfile']
    
            if (new_title != "") and (new_author != ""):
        
                fs = FileSystemStorage()
                filename = fs.save(myfile.name, myfile)
                uploaded_file_url = fs.url(filename)

                new_book = Book(title=new_title,author=new_author,category=new_cat,avg_rating="0.0",img="/media/"+myfile.name)
                new_book.save()

        
          
                message = "successful!!"
        
            else:
                message = "unsuccessful."

    except MultiValueDictKeyError:
        message = "unsuccessful."

    context = {
        'message' : message,
    }
    template = loader.get_template('bookstore/addnewbook.html')
    return HttpResponse(template.render(context, request))

    
