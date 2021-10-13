from django import http
from django.http.response import HttpResponse
from django.shortcuts import render
from blog .models import Post 
# Create your views here.


def home(request):
    
    allPosts= Post.objects.all()
    print(allPosts)
    context={'allPosts': allPosts}
    return render(request,'blog/bloghome.html', context)



def blogPost(request, slug):

    post= Post.objects.filter(slug=slug).first()
    print(post)
    context={"post": post}
    return render (request,'blog/blogPost.html') 







