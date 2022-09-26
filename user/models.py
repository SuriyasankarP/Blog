from statistics import mode
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import date,datetime
from ckeditor.fields import RichTextField




# Create your models here.
class Category(models.Model):
    name=models.CharField(max_length=255)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse ('home')


class Post(models.Model):
    title=models.CharField(max_length=255)
    titleTag=models.CharField(max_length=255)
    header_image=models.ImageField(null=True,blank=True,upload_to="images/")
    author=models.ForeignKey(User,on_delete=models.CASCADE)
    snippet=models.TextField(max_length=255,default='Click link above to view post....')
    category=models.CharField(max_length=255,default='Uncategory')
    body=RichTextField(blank=True,null=True)
    post_date=models.DateField(auto_now_add=True)
    likes=models.ManyToManyField(User,related_name='blog_post')

    def total_like(self):
        return self.likes.count()

    def __str__(self):
        return self.title + " " + str(self.author)
    
    def get_absolute_url(self):
        return reverse ('home')
