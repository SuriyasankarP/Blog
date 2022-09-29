from django.shortcuts import render,redirect,get_object_or_404
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from user.models import Post,Category,Comment
from django.contrib import messages
from .form import PostForm,EditForm,PostCommentForm
from django.urls import reverse_lazy,reverse
from urllib import request
from datetime import date,datetime
from django.http import HttpResponseRedirect

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

    def get_context_data(self,*args,**kwargs):
        cat_menu=Category.objects.all()
        context=super(ArticleView, self).get_context_data()
        stuff =get_object_or_404(Post,id=self.kwargs['pk'])
        

        liked=False
        if stuff.likes.filter(id=self.request.user.id).exists():
            liked=True
        context['liked']=liked

        return context



"""class CategoryView(ListView):
    #cats1=cats.replace('-',' ')
    model = Post
    template_name = 'category.html'
    def get_queryset(self):
        return Post.objects.filter(category=self.kwargs.get('cats'),)"""
def CategoryView(request,cats):
    
    category_post=Post.objects.filter(category=cats)
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
    form_class=EditForm
    
class DeleteArticle(DeleteView):
    model=Post
    template_name='deleteArticle.html'
    success_url=reverse_lazy('home')

def LikeView(request, pk):
    #post=get_object_or_404(Post,id=kwargs['pk'])
    post=Post.objects.get(id=pk)
    liked=False
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
        liked=False
    else:
        post.likes.add(request.user)
        liked=True
    return HttpResponseRedirect(reverse('article',args=[str(pk)]))

class AddCommentView(CreateView):
    model=Comment
    form_class=PostCommentForm
    template_name='add_comments.html'
    

    def form_valid(self,form):
        form.instance.post_id=self.kwargs['pk']
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('article', kwargs={'pk': self.kwargs['pk']})

"""def AddCommentView(request,pk):
    post=Post.objects.get(id=pk)
    user_name=User.objects.get(id=pk)


    form=PostCommentForm(instance=post)

    if request.method=='POST':
        form=PostCommentForm(request.POST, instance=post)
        if form.is_valid():
            name=user_name
            body=form.cleaned_data['comment']
            c =Comment(post=post,name=name,comments=body,date_added=datetime)
            c.save()

            return redirect('article',pk=pk)

        else:
            print("form is invalid")    
    else:
        form=PostCommentForm()

    context={
    'form' : form
    }

    return render(request,'add_comments.html',context) """



def delete_comment(request,pk):
    comment= Comment.objects.filter(post=pk)
    comment.delete()
    return redirect('article',pk=pk)


