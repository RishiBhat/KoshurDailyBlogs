from django.db import models
from django.db.models.fields import DateTimeField

# Create your models here.

class Blog(models.Model):
    First_name=models.CharField(max_length=5000),
    last_name=models.CharField(max_length=6000),
    sno=models.AutoField(primary_key=True),
    email=models.CharField(max_length=6000),
    phone=models.IntegerField(default=8000),

    def __str__(self):
        return self.First_name


class Author(models.Model):
    First_name=models.CharField(max_length=5000),
    number=models.AutoField(primary_key=True),
    phone=models.IntegerField(default=8000),
    name=models.CharField(max_length=5000),

    def __str__(self):
        return self.First_name





class Book(models.Model):
    Book_name=models.CharField(max_length=5000),
    BookNumber= models.IntegerField(default=8000),
    No_of_Articles=models.IntegerField(default=8000),
    Book=models.AutoField(primary_key=True),

    def __str__(self):
        return self.Book_name

class Articles(models.Model):
    Article=models.CharField(max_length=500),
    No_of_Articles=models.IntegerField(default=5000),
    publish_date=models.DateTimeField(DateTimeField()),

    def __str__(self):
        return self.Article