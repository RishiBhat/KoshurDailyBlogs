from typing import TYPE_CHECKING
from django.db.models.lookups import PostgresOperatorLookup
from django.http.request import HttpRequest
from django.shortcuts import render, HttpResponse
from home.models import Contact 
from blog.models import Post

# Create your views here.

from django.contrib import messages     


def home(request):
    return render (request,'home/home.html')

def about(request):
    return render(request, 'home/about.html')
 
def contact(request):

    messages.success(request, 'Thanks for joining the iKoshur Page here')
    if request.method == 'POST':
        name = request.POST ['name']
        phone = request.POST['phone']
        email = request.POST['email']
        desc = request.POST['desc']
        print(name, phone, email , desc)


        if len(name)<2 or len(email)<3 or len(phone)<10 or len(desc)<4:
            messages.error(request, "Please fill up the form correct ass")
        else:
            contact= Contact( name=name,email=email , phone=phone, content=desc)
            contact.save()
            messages.success(request, 'your message has been said ') 

    return render(request, 'home/contact.html')


def search(request):
    query=request.GET['query']
    if len(query)>78:
        allPosts=Post.objects.none()
    else:
        allPostsTitle= Post.objects.filter(title__icontains=query)
        allPostsAuthor= Post.objects.filter(author__icontains=query)
        allPostsContent =Post.objects.filter(content__icontains=query)
        allPosts=  allPostsTitle.union(allPostsContent, allPostsAuthor)
    if allPosts.count()==0:
        messages.warning(request, "No search results found. Please refine your query.")
    params={'allPosts': allPosts, 'query': query}
    return render(request, 'home/search.html', params)

