from django.db import models
from django.core.files.storage import FileSystemStorage

# Create your models here.
class registrationList(models.Model):
    username=models.CharField(max_length=300,)
    usermail=models.CharField(max_length=300, blank=False,unique=True)
    pass1=models.CharField(max_length=32)
    pass2=models.CharField(max_length=32)
    varsity=models.CharField(max_length=100)
    lovebooktype=models.CharField(max_length=200)
    userimage=models.FileField()
    time=models.DateTimeField()
    
class userimage(models.Model):
    usermail=models.CharField(max_length=300, blank=False)
    userimage=models.FileField()
    time=models.CharField(max_length=300, blank=False)
    
class publicallpost(models.Model):
    usermail=models.CharField(max_length=300, blank=False)
    booktitle=models.CharField(max_length=200)
    bookwritter=models.CharField(max_length=200)
    userphone=models.CharField(max_length=100)
    usercomment=models.TextField(max_length=500)
    usercontactinfo=models.TextField(max_length=400)
    bookprice=models.CharField(max_length=20)
    useroption=models.CharField(max_length=30)
    bookimage=models.FileField()
    bookview=models.IntegerField()
    time=models.DateTimeField()
    
class user_personal_post(models.Model):
    usermail=models.CharField(max_length=200, blank=False)
    postuniqid=models.IntegerField()