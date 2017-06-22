from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect,HttpResponse
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from django.template import loader
from .models import Book,Review,Category
from django.db.models import Count,Max,Avg
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.utils.datastructures import MultiValueDictKeyError
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
import datetime

def home(request,user_name):
   
    num_books = Book.objects.filter(owner=user_name).count()
    latest_book = Book.objects.filter(owner=user_name).order_by('-id')[:5]
    latest_review =Book.objects.filter(owner=user_name).order_by('-update_review')[:5]
    top5book = Book.objects.filter(owner=user_name).order_by('-avg_rating')[:5]
    choice_cat = Category.objects.filter(owner=user_name)
    num_review=[]

    for i in top5book:

        num_review.append(Review.objects.filter(book=i).count())

    top5rating = zip(top5book, num_review)
    template = loader.get_template('bookstore/home.html')
    context = {
        'latest_book' : latest_book,
        'num_books' : num_books,
        'latest_review' : latest_review,
        'top_five_rating' : top5rating,
        'choice_cat' : choice_cat,
        'user_name' : user_name,
        
    }
    return HttpResponse(template.render(context, request))
    
def category(request,cat,user_name):
    choice_cat = Category.objects.all()
    if cat == 'Allbooks':
        book = Book.objects.filter(owner=user_name).order_by('title')
        
    else:
        book = Book.objects.filter(owner=user_name, category__name=cat).order_by('title')

        
    template = loader.get_template('bookstore/category.html')
    context = {
       'book' : book,
       'cat' : cat,
       'choice_cat' : choice_cat,
       'user_name' : user_name,
    }
    return HttpResponse(template.render(context, request))

def display_title(request,book_id,user_name):
    book_name = get_object_or_404(Book, pk=book_id)
    book_review = Review.objects.filter(book=book_name).order_by('-timestamp')[:5]
    image = Book.objects.filter(pk=book_id)
    choice_cat = Category.objects.all()
  
    
    template = loader.get_template('bookstore/display_title.html')
    context = {
        'book_name' : book_name,
        'book_review' : book_review,
        'image' : image,
        'choice_cat' : choice_cat,
        'user_name' : user_name,
    }
    return HttpResponse(template.render(context, request))


def review(request,book_id,user_name):
    book_name = Book.objects.filter(id=book_id)
    new_review_message = request.POST.get('review_message')
    new_rating = request.POST.get('rating')
    book_review = Review.objects.filter(book=book_name)
    
    
    if (new_review_message != "") and (new_rating != None):
        
        for a in book_name: 

            new_review = Review(book=a,timestamp=timezone.now(),review_message=new_review_message,rating=new_rating)
            new_review.save()

            avg = Book.objects.filter(id=book_id).update(avg_rating = Review.objects.filter(book=book_name).aggregate(Avg('rating')).get('rating__avg', 0.00))
            update = Book.objects.filter(id=book_id).update(update_review = timezone.now())
        
        return HttpResponseRedirect('/%s/%s/' %(user_name,book_id))
    else:
        
        book_name = get_object_or_404(Book, pk=book_id)
        book_review = Review.objects.filter(book=book_name).order_by('-timestamp')[:5]
        image = Book.objects.filter(pk=book_id)
  
    
        template = loader.get_template('bookstore/display_title.html')
        context = {
            'book_name' : book_name,
            'book_review' : book_review,
            'image' : image,
            'message' : "your review unsuccessful.",
            'user_name' : user_name,
        }
        return HttpResponse(template.render(context, request))
        
    
 

def display_allreviews(request,user_name):
    allreviews = latest_review = Review.objects.all().order_by('-id')
    template = loader.get_template('bookstore/allreviews.html')
    context = {
        'allreviews' : allreviews,
        'user_name' : user_name,
    }
    return HttpResponse(template.render(context, request))

def search(request,user_name):
    choice_cat = Category.objects.all()
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
        'choice_cat':choice_cat,
        'search_query' : search_query,
        'user_name' : user_name,
    }
    return HttpResponse(template.render(context, request))

def about(request,user_name):
    choice_cat = Category.objects.all()
    template = loader.get_template('bookstore/about.html')
    return HttpResponse(template.render({'choice_cat':choice_cat,'user_name':user_name}, request))

def newbook(request,user_name):
    choice_cat = Category.objects.all()
    template = loader.get_template('bookstore/newbook.html')
    return HttpResponse(template.render({'choice_cat':choice_cat,'user_name' : user_name,}, request))
    
def addnewbook(request,user_name):
    choice_cat = Category.objects.all()
    messaage=""
    new_cate=""
    try:
        if request.method == 'POST' and request.FILES['myfile']:
            new_title = request.POST.get('title')
            new_author = request.POST.get('author')
            new_cat = request.POST.get('cat')
            myfile = request.FILES['myfile']
            

            if new_cat=="others":
                new_cate = request.POST.get('catt')
                new_category = Category(name=new_cate,owner=user_name)
                new_category.save()
                
            else:
                new_cate = request.POST.get('cat')

            new_cate = Category.objects.filter(name=new_cate)

            if (new_title != "") and (new_author != ""):
                fs = FileSystemStorage()
                filename = fs.save(myfile.name, myfile)
                uploaded_file_url = fs.url(filename)
                for a in new_cate:
                    new_book = Book(title=new_title,author=new_author,category=a,avg_rating="0.0",img="/media/"+myfile.name,owner=user_name)
                    new_book.save()
        
          
                return HttpResponseRedirect('/%s/' %(user_name))
        
            else:
                message = "unsuccessful."

    except MultiValueDictKeyError:
        message = "unsuccessful."

    context = {
        'message' : message,
        'choice_cat':choice_cat,
        'user_name' : user_name,
    }
    template = loader.get_template('bookstore/addnewbook.html')
    return HttpResponse(template.render(context, request))

def index(request):
    
    return render(request,"bookstore/login.html",[])


def checklogin(request):
    uname = request.POST['uname']
    upassword = request.POST['password']
    user = authenticate(username=uname,password=upassword)
    
    if user is not None:
        #login(request,user)
        return HttpResponseRedirect('/%s/' %(uname) )
    else:
        return HttpResponse("Error invalid login.")  

def register(request):

    return render(request,"bookstore/register.html",[])

def registeration(request):
    uname = request.POST['uname']
    upassword = request.POST['password']
    umail = request.POST['umail']
    message = ""
    if uname != "" and upassword != "" and umail != "" and uname != "admin":
        user = User.objects.create_user(username=uname,email=umail,password=upassword)
        message = "successful"
        
    else:
        message = "unsuccessful"
    context = {
        'message' : message,
    }    
    template = loader.get_template('bookstore/register.html')
    return HttpResponse(template.render(context, request))

def logout_view(request,user_name):
    logout(request)

    return HttpResponseRedirect('/')
