
from django.urls import path,include
from .views import BlogView,ArticleView,AddArticle,UpdateArticle,DeleteArticle,AddCategory,CategoryView,CategoryView,CategoryListView

urlpatterns = [

    path('',BlogView.as_view(), name="home"),
    path('article/<int:pk>',ArticleView.as_view(),name='article'),
    path('add/',AddArticle.as_view(), name="add"),
    path('add_category/',AddCategory.as_view(), name="add_category"),
    path('article/edit/<int:pk>',UpdateArticle.as_view(),name="update"),
    path('article/delete/<int:pk>',DeleteArticle.as_view(),name='delete'),
    path('category/<str:cats>',CategoryView,name='category'),
    path('category/',CategoryListView.as_view(),name='categoryList')
   ]