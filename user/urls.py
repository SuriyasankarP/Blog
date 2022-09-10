
from django.urls import path,include
from .views import BlogView,ArticleView,AddArticle

urlpatterns = [

    path('',BlogView.as_view(), name="home"),
    path('article/<int:pk>',ArticleView.as_view(),name='article'),
    path('add/',AddArticle.as_view(), name="add"),

]