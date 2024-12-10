from django.shortcuts import render,HttpResponse,redirect
from .models import Post
from .forms import PostForm
from django.contrib import messages

# Create your views here.
def post_index(request):
    posts = Post.objects.all()
    return render(request,'posts/index.html',{'posts':posts})
def add_post(request):
    form = PostForm()
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your post has been added.')
    form = PostForm()

    return render(request,'posts/CreatePost.html',{'form':form})

def upd_post(request,post_id):
   ## post=Post.objects.get(id=request.GET['post_id'])
   post = Post.objects.get(id=post_id)
   form = PostForm(instance=post)
   if request.method == 'POST':
       form = PostForm(request.POST, instance=post)
       if form.is_valid():
           form.save()
           messages.success(request, 'Your post has been updated.')
   return render(request,"posts/UpdatePost.html",{'form':form})
def post_detail(request,post_id):
    post=Post.objects.get(id=post_id)
    return render(request,"posts/detail.html",{'post':post})
def del_post(request,post_id):
    post = Post.objects.get(id=post_id)
    post.delete()
    messages.success(request, 'Your post has been deleted.')
    return redirect('/posts')