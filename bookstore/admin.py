from django.contrib import admin

from .models import Book,Review,Category

admin.site.register(Book)
admin.site.register(Review)
admin.site.register(Category)
