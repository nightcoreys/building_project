from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^checkaccount/$', views.checkaccount, name='checkaccount'),
    url(r'^$', views.index, name='index'),
    url(r'^register/$', views.register, name='register'),
    url(r'^(?P<user_name>\w+)/about/$', views.about, name='about'),
    url(r'^registeration/$', views.registeration, name='registeration'),
    url(r'^(?P<user_name>\w+)/logout/$', views.logout_view, name='logout'),
    url(r'^(?P<user_name>\w+)/$', views.home, name='home'),
    url(r'^(?P<user_name>\w+)/cat/(?P<cat>[a-zA-Z]+)/$', views.category, name='category'),
    url(r'^(?P<user_name>\w+)/(?P<book_id>[0-9]+)/$', views.display_title, name='display_title'),
    url(r'^(?P<user_name>\w+)/(?P<book_id>[0-9]+)/review/$', views.review, name='review'),
    url(r'^(?P<user_name>\w+)/allreviews/$', views.display_allreviews, name='review'),
    url(r'^(?P<user_name>\w+)/search/$', views.search, name='search'),
    url(r'^(?P<user_name>\w+)/addnewbook/$', views.addnewbook, name='addnewbook'),
    url(r'^(?P<user_name>\w+)/newbook/$', views.newbook, name='newbook'),
    

]
