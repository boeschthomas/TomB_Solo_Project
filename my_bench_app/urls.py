from django.urls import path     
from . import views
urlpatterns = [
    path('', views.index),
    path('register', views.register),
    path('home', views.home),
    path('login', views.login),
    path('my_page/<int:id>', views.my_page),
    path('comm_page/<int:id>', views.comm_page),
    path('create_page', views.create_page)	   
]
