from django.shortcuts import render,redirect
from django.views.generic import ListView,DetailView,CreateView
from user.models import Post
from django.contrib import messages

class BlogView(ListView):
    model = Post
    template_name='home.html'

class ArticleView(DetailView):
    model =Post
    template_name='article.html'

class AddArticle(CreateView):
    model=Post
    template_name='addArticle.html'
    fields='__all__'





