from django import forms
from .models import Post,Category


choices=Category.objects.all().values_list('name','name')

choices_list=[]

for item in choices:
	choices_list.append(item)


class PostForm(forms.ModelForm):
	class Meta:
		model = Post
		fields=['title','titleTag','author','category','body']

		widgets ={
		'title' : forms.TextInput(attrs={'class': 'form-control'}),
		'titleTag' : forms.TextInput(attrs={'class': 'form-control'}),
		'author' : forms.TextInput(attrs={'class': 'form-control','value' : "",'id': "current" ,'type' : 'hidden'}),
		#'author' : forms.Select(attrs={'class': 'form-control'}),
		'category' : forms.Select(choices=choices,attrs={'class': 'form-control'}),
		'body' : forms.Textarea(attrs={'class': 'form-control','placeholder' :'Must Be In HTML Format'}),
		}

class EditForm(forms.ModelForm):
	class Meta:
		model = Post
		fields='__all__'

		widgets ={
		'title' : forms.TextInput(attrs={'class': 'form-control'}),
		'titleTag' : forms.TextInput(attrs={'class': 'form-control'}),
		'author' : forms.Select(attrs={'class': 'form-control'}),
		'category' : forms.Select(choices=choices_list,attrs={'class': 'form-control'}),
		'body' : forms.Textarea(attrs={'class': 'form-control','placeholder' :'Must Be In HTML Format'}),
		}