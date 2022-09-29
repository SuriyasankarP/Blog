from django.shortcuts import render,get_object_or_404
from django.views.generic import CreateView,UpdateView,DetailView
from django.contrib.auth.forms import UserCreationForm,UserChangeForm,PasswordChangeForm
from django.urls import reverse_lazy
from django.contrib.auth.views import PasswordChangeView
from .forms import SignUpForm,EditProfile,ChangePasswordForm,ProfileCreateForm,ProfileEditForm
from django.contrib.messages import constants as messages
from user.models import Profile
from django.shortcuts import render,redirect
from django.contrib import messages



class CreateProfilePageView(CreateView):
	model=Profile
	form_class=ProfileCreateForm

	template_name='registration/create_profile-page.html'
	success_url=reverse_lazy('home')


	def form_valid(self,form):
		form.instance.user=self.request.user
		return super().form_valid(form)
	


class ProfileEditView(UpdateView):
	model=Profile
	form_class= ProfileEditForm
	template_name="registration/edit_profile_page.html"
	#fields=['bio','profile_pic','facebook_url','Instagram_url','linkedin_url']
	success_url=reverse_lazy('home')

class ProfileView(DetailView):
	model = Profile
	template_name='registration/profile_view.html'
	
	def get_context_data(self,*args,**kwargs):
		user=Profile.objects.all()
		context=super(ProfileView, self).get_context_data(**kwargs)
		page_user =get_object_or_404(Profile,id=self.kwargs['pk'])
		context['page_user']=page_user
		return context


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
"""def UserRegister(request):
    if request.method=="POST":
        form = SignUpForm(request.POST or None)
        if form.is_valid():
            form.save()
        else:
	        messages.success(request, ('Your Form Has Been Submited'))
		    return redirect ('register')

	    messages.success(request, ('There is an error...Try again'))
        return redirect('register')
    else:
        return render(request,'registration/register.html',{})"""
class UserEdit(UpdateView):
	form_class=EditProfile
	template_name='registration/edit_profile.html'
	success_url=reverse_lazy('home')
	
	def get_object(self):
		return self.request.user
	
	

