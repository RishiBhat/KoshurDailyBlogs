from django.db import models

# Create your models here.



class Post(models.Model):
    sno=models.CharField(max_length=5000)
    title=models.CharField(max_length=5000)
    author=models.CharField(max_length=5000)
    slug=models.CharField(max_length=5000)
    timeStamp=models.DateTimeField(blank=True)
    content=models.TextField() 


    def __str__ (self): 
        return self.title + " by " + self.author