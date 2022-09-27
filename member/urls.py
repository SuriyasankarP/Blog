from django.urls import path,include
from .views import ProfileView,UserRegister,UserEdit,PasswordsChangeView,ProfileEditView,CreateProfilePageView
from django.contrib.auth import views as auth_views
from . import views
urlpatterns = [
    path('register/',UserRegister.as_view(),name='register'),
    path('edit_profile/',UserEdit.as_view(),name='edit_profile'),
    #path('password/', auth_views.PasswordChangeView.as_view(template_name='registration/change-password.html'))
    path('password/',PasswordsChangeView.as_view(template_name='registration/change-password.html')),
   
    path('password_success',views.PasswordSuccess,name='PResetSucess'),
    path('<int:pk>/profile',ProfileView.as_view(),name='profile_page'),
    path('<int:pk>/profile_edit',ProfileEditView.as_view(),name='profile_page_edit') ,
    path('profile_create',CreateProfilePageView.as_view(),name='profile_page_create')   

]