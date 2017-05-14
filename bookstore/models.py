from django.db import models
from django.utils import timezone
import datetime

class Book(models.Model):
    title = models.CharField(max_length=255,null=False)
    author = models.CharField(max_length=255,null=False)
    category = models.CharField(max_length=256, choices=[('Comics', 'Comics'), ('Novel', 'Novel'),('Psychology','Psychology')]) 
    avg_rating = models.FloatField(default=0.0)
    img = models.CharField(max_length=100,null=False)
    update_review = models.DateTimeField(null=True)
    release_date = models.DateTimeField(default=timezone.now())

    def __str__(self):
        return self.title
    

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
    



