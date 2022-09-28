from django import forms
from .models import Post,Category,Comment


choices=Category.objects.all().values_list('name','name')

choices_list=[]

for item in choices:
	choices_list.append(item)


class PostForm(forms.ModelForm):
	class Meta:
		model = Post
		fields=['title','titleTag','author','category','snippet','body']

		widgets ={
		'title' : forms.TextInput(attrs={'class': 'form-control'}),
		'titleTag' : forms.TextInput(attrs={'class': 'form-control'}),
		'author' : forms.TextInput(attrs={'class': 'form-control','value' : "",'id': "current" ,'type' : 'hidden'}),
		'header_image' : forms.FileInput(attrs = {'class': 'form-control', "id" : "image_field"}),
		#'author' : forms.Select(attrs={'class': 'form-control'}),
		'category' : forms.Select(choices=choices,attrs={'class': 'form-control'}),
		'snippet' : forms.Textarea(attrs={'class': 'form-control'}),
		'body' : forms.Textarea(attrs={'class': 'form-control','placeholder' :'Must Be In HTML Format'}),
		}

class EditForm(forms.ModelForm):
	class Meta:
		model = Post
		fields=['title','titleTag','category','snippet','body']

		widgets ={
		'title' : forms.TextInput(attrs={'class': 'form-control'}),
		'titleTag' : forms.TextInput(attrs={'class': 'form-control'}),
	
		'category' : forms.Select(choices=choices_list,attrs={'class': 'form-control'}),
		'snippet' : forms.Textarea(attrs={'class': 'form-control'}),
		'body' : forms.Textarea(attrs={'class': 'form-control','placeholder' :'Must Be In HTML Format'}),
		}

class PostCommentForm(forms.ModelForm):
	class Meta:
		model = Comment
		fields=['name','comment']

		widgets ={
		'name' : forms.TextInput(attrs={'class': 'form-control'}),
		'comment' : forms.Textarea(attrs={'class': 'form-control'}),
		
		}