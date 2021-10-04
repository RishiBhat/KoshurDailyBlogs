#This url willl be made by the user for the app urls 

#This is copy pasted from  the admin file here 
from django.contrib import admin
from django.urls.conf import include
from django.urls import path
from .import views 

urlpatterns = [

    path('',views.index, name='home'),
    path('about/',views.about,name='revrishi/home.html'), 
    path('services/',views.services,name="This is the service page"),
    path('blog/',views.blog,name='Blogs'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('author',views.authors, name='Authors'),
    path('contact',views.contact, name="Contact"),
    path('articles',views.articles, name="Article"),

] 

