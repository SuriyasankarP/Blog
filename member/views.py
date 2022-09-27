from django.shortcuts import render
from django.views.generic import CreateView,UpdateView
from django.contrib.auth.forms import UserCreationForm,UserChangeForm,PasswordChangeForm
from django.urls import reverse_lazy
from django.contrib.auth.views import PasswordChangeView
from .forms import SignUpForm,EditProfile,ChangePasswordForm
from django.contrib.messages import constants as messages



class PasswordsChangeView(PasswordChangeView):
	#form_class=PasswordChangeForm
	form_class=ChangePasswordForm
	success_url=reverse_lazy('PResetSucess')
def PasswordSuccess(request):
	return render (request,'registration/password_success.html',{})

class UserRegister(CreateView):
	form_class=SignUpForm
	template_name='registration/register.html'
	success_url=reverse_lazy('login')
	

class UserEdit(UpdateView):
	form_class=EditProfile
	template_name='registration/edit_profile.html'
	success_url=reverse_lazy('home')

	def get_object(self):
		return self.request.user
	
	

