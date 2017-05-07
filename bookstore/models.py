from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    category = models.CharField(max_length=256, choices=[('Comics', 'Comics'), ('Novel', 'Novel'),('Psychology','Psychology')]) 
    available = models.BooleanField(default=True)
    avg_rating = models.FloatField(default=0.0)
    img = models.CharField(max_length=100,default="/static/bookstore/images.png")

    def __str__(self):
        return self.title
    

#class ImageBook(models.Model):
#    mainimage = models.ImageField(upload_to='img', null = True)
#    image = models.ForeignKey(Book)

class Review(models.Model):

    book = models.ForeignKey(Book)
    timestamp = models.DateTimeField()
    review_message = models.CharField(max_length=500)
    rating = models.IntegerField(
        choices=(
            (1, '1'),
            (2, '2'),
            (3, '3'),
            (4, '4'),
            (5, '5'),
        )
    )

    def __str__(self):
        return self.book.title

    

class User(models.Model):
    username = models.CharField(max_length=255,primary_key=True)
    password = models.CharField(max_length=255)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)

    def __str__(self):
        return self.username


