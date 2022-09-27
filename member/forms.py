from django.contrib.auth.forms import UserCreationForm,UserChangeForm,PasswordChangeForm
from django.contrib.auth.models import User
from django import forms
from user.models import Profile


class SignUpForm(UserCreationForm):
	email=forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
	first_name =forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class': 'form-control'}))
	last_name =forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class': 'form-control'}))
	


	class Meta:
		model=User
		fields=('username','first_name','last_name','email','password1','password2')



	def __init__(self,*args,**kwargs):
		super(SignUpForm, self).__init__(*args,**kwargs)
		self.fields['username'].widget.attrs['class']='form-control'
		self.fields['password1'].widget.attrs['class']='form-control'
		self.fields['password2'].widget.attrs['class']='form-control'

class EditProfile(UserChangeForm):
	email=forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
	first_name =forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class': 'form-control'}))
	last_name =forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class': 'form-control'}))
	username =forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class': 'form-control'}))
	
	#last_login =forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class': 'form-control'}))
	#is_superuser =forms.CharField(max_length=100,widget=forms.CheckboxInput(attrs={'class': 'form-check'}))
	#is_staff =forms.CharField(max_length=100,widget=forms.CheckboxInput(attrs={'class': 'form-check'}))
	#is_active =forms.CharField(max_length=100,widget=forms.CheckboxInput(attrs={'class': 'form-check'}))
	#date_joined =forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class': 'form-control','type' : 'hidden'}))

	class Meta:
		model=User
		fields=('username','first_name','last_name','email', )



class ChangePasswordForm(PasswordChangeForm):
	old_password=forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control','type' : 'password'}))
	new_password1=forms.CharField(max_length=100,widget=forms.PasswordInput(attrs={'class': 'form-control','type' : 'password'}))
	new_password2=forms.CharField(max_length=100,widget=forms.PasswordInput(attrs={'class': 'form-control','type' : 'password'}))

	class Meta:
		model=User
		fields=('old_password','new_password1','new_password2')

class ProfileCreateForm(forms.ModelForm):
	class Meta:
		model = Profile
		fields=['profile_pic','bio','facebook_url','Instagram_url','linkedin_url','user']

		widgets ={
		'bio' : forms.TextInput(attrs={'class': 'form-control'}),
		'facebook_url' : forms.TextInput(attrs={'class': 'form-control'}),
		'user' : forms.TextInput(attrs={'class': 'form-control','value' : "",'id': "current" ,'type' : 'hidden'}),
		'profile_pic' : forms.FileInput(attrs = {'class': 'form-control', "id" : "image_field"}),
		#'author' : forms.Select(attrs={'class': 'form-control'}),
		'Instagram_url' : forms.TextInput(attrs={'class': 'form-control'}),
		'linkedin_url' : forms.TextInput(attrs={'class': 'form-control'}),
		
		}
class ProfileEditForm(forms.ModelForm):
	class Meta:
		model = Profile
		fields=['profile_pic','bio','facebook_url','Instagram_url','linkedin_url']

		widgets ={
		'bio' : forms.TextInput(attrs={'class': 'form-control'}),
		'facebook_url' : forms.TextInput(attrs={'class': 'form-control'}),
		'profile_pic' : forms.FileInput(attrs = {'class': 'form-control', "id" : "image_field"}),
		#'author' : forms.Select(attrs={'class': 'form-control'}),
		'Instagram_url' : forms.TextInput(attrs={'class': 'form-control'}),
		'linkedin_url' : forms.TextInput(attrs={'class': 'form-control'}),
		
		}