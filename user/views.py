from django.shortcuts import render,redirect
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from user.models import Post,Category
from django.contrib import messages
from .form import PostForm
from django.urls import reverse_lazy
from urllib import request

class BlogView(ListView):
    model = Post
    template_name='home.html'
    ordering=['-post_date']
class CategoryListView(ListView):
    model = Category
    template_name='categorylist.html'
    
class ArticleView(DetailView):
    model =Post
    template_name='article.html'


"""class CategoryView(ListView):
    #cats1=cats.replace('-',' ')
    model = Post
    template_name = 'category.html'
    def get_queryset(self):
        return Post.objects.filter(category=self.kwargs.get('cats'),)"""
def CategoryView(request,cats):
    
    category_post=Post.objects.filter(category=cats.replace('-',' '))
    return render (request,'category.html',{'cats' : cats,'category_post' : category_post})

class AddArticle(CreateView):
    model=Post
    form_class=PostForm
    template_name='addArticle.html'

class AddCategory(CreateView):
    model=Category
    template_name='addCategory.html'
    fields='__all__'

class UpdateArticle(UpdateView):
    model=Post
    template_name='updateArticle.html'
    form_class=PostForm
    
class DeleteArticle(DeleteView):
    model=Post
    template_name='deleteArticle.html'
    success_url=reverse_lazy('home')





