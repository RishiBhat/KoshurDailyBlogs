
from django.http import request
from django.shortcuts import render, HttpResponse


# Create your my views here for staisying the url link given in the url.py of the app 


#This is file got redirected from the app/urls.py because of the {path ('',views.index,"Thios is home")}
def index(request):      
    return render (request,'home/home.html')

def articles(request):
    return render(request,'home/articles.html')
def about(request):
    return render(request,"home/home.html")


def contact(request):
    return render(request, "home/contact/html") 
def blog(request):
    return render(request, 'home/home.html')


def authors(request):
    return render(request, 'home/home.html')

def services(request):
    return HttpResponse ("revrishi/index.html")

def dashboard(request):
    return render(request, 'home/home/html')


