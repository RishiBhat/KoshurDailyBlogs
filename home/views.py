#playing up with the import export files in the django and printing out the pdf files here!!


import io 
from django.http import FileResponse, response
from reportlab.pdfgen import canvas


#---------------------------------------->



#creating a openpyxl library to import and export the workbook 

from django.http import HttpResponse
from django.contrib.auth.models import User 
import xlwt


#-----------------------------------------> 


from django.shortcuts import render, HttpResponse, redirect
from home.models import Contact
from django.contrib import messages 
from django.contrib.auth.models import User 
from django.contrib.auth  import authenticate,  login, logout
from blog.models import Post

def home(request): 
    return render(request, "home/home.html")

def contact(request):
    if request.method=="POST":
        name=request.POST['name']
        email=request.POST['email']
        phone=request.POST['phone']
        content =request.POST['content']
        if len(name)<2 or len(email)<3 or len(phone)<10 or len(content)<4:
            messages.error(request, "Please fill the form correctly")
        else:
            contact=Contact(name=name, email=email, phone=phone, content=content)
            contact.save()
            messages.success(request, "Your message has been successfully sent")
    return render(request, "home/contact.html")

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

def handleSignUp(request):
    if request.method=="POST":
        # Get the post parameters
        username=request.POST['username']
        email=request.POST['email']
        fname=request.POST['fname']
        lname=request.POST['lname']
        pass1=request.POST['pass1']
        pass2=request.POST['pass2']

        # check for errorneous input
        if len(username)<10:
            messages.error(request, " Your user name must be under 10 characters")
            return redirect('home')

        if not username.isalnum():
            messages.error(request, " User name should only contain letters and numbers")
            return redirect('home')
        if (pass1!= pass2):
             messages.error(request, " Passwords do not match")
             return redirect('home')
        
        # Create the user
        myuser = User.objects.create_user(username, email, pass1)
        myuser.first_name= fname
        myuser.last_name= lname
        myuser.save()
        messages.success(request, " Your iCoder has been successfully created")
        return redirect('home')

    else:
        return HttpResponse("404 - Not found")


def handeLogin(request):
    if request.method=="POST":
        # Get the post parameters
        loginusername=request.POST['loginusername']
        loginpassword=request.POST['loginpassword']

        user=authenticate(username= loginusername, password= loginpassword)
        if user is not None:
            login(request, user)
            messages.success(request, "Successfully Logged In")
            return redirect("home")
        else:
            messages.error(request, "Invalid credentials! Please try again")
            return redirect("home")

    return HttpResponse("404- Not found")
   

    return HttpResponse("login")

def handelLogout(request):
    logout(request)
    messages.success(request, "Successfully logged out")
    return redirect('home')


def about(request): 
    return render(request, "home/about.html")




def some_view(request):
    #creating a dummy  ffile to recieve the data from the file 
    buffer = io.BytesIO()



    #creating the pdf object with buffer as its file 

    p = canvas.Canvas(buffer)

    #draw the things on the pdf, here's what the pdf generation happens 

    #see the reportlabdocumentation for the full list of  functionality 


    p.drawString(100,100, "Hello this is iKoshur world")
    #close the pdf cleanly and we are done

    p.showPage()
    p.save()


    buffer.seek(0)
    return FiileResponse(buffer, as_attachment=True, filename='start.pdf')





#we  created the django-admin export file here

def export_users_csv(request):
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="users.xls"'

    wb= xlwt.Workbook(encoding='utf-8')
    ws= wb.add_sheet('Users Data')


    row_num = 0
    font_style = xlwt.XFStyle()
    font_style.font.bold=True

    columns= ['Username', 'First Name', 'Last Name', 'Email Address']

    for col_num in range (len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style)

    font_style = xlwt.XFStyle()


    rows = User.objects.all().values_list('username','first_name','last_name','email')

    for row in rows: 
        row_num +=1 
        for col_num in range(len(row)):
            ws.write(row_num, col_num, row[col_num], font_style)
    wb.save(response)
    return response