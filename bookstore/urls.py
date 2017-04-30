from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^home/$', views.home, name='index'),
    url(r'^cat/(?P<cat>[a-zA-Z]+)/$', views.category, name='category'),
    url(r'^(?P<book_id>[0-9]+)/$', views.display_title, name='display_title'),
    url(r'^reserve/(?P<book_id>[0-9]+)/$', views.reserve, name='reserve'),
    url(r'^review/(?P<book_id>[0-9]+)/$', views.review, name='review'),
    url(r'^$', views.login, name='login'),
    url(r'^login/$', views.checklogin, name='checklogin'),
    url(r'^allreviews/$', views.display_allreviews, name='review'),
    url(r'^search/$', views.search, name='search'),

]
