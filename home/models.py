from django.db import models
from django.db.models.fields import EmailField
from django.http import FileResponse
from reportlab.pdfgen import canvas


# Create your models here.



#create your mdodel


class Contact(models.Model):
    sno=models.AutoField(primary_key=True)
    name=models.CharField(max_length=5000)
    phone=models.IntegerField(default=5000)
    email=models.CharField(max_length=500)
    content= models.TextField()
    timestamp= models.TimeField (auto_now_add=True, blank=True)

    def __str__ (self):
        return self.name



