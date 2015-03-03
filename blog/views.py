from django.shortcuts import render, get_object_or_404, redirect
from .models import Post
from django.utils import timezone 
from .forms import PostForm
from django.contrib.auth import authenticate, login

def post_list (request):
	user = authenticate(username='e-zrra', password='password')
	login(request, user)
	posts = Post.objects.all();
	return render(request, 'blog/post_list.html', { 'posts' : posts })

def post_detail (request, pk):
	post = get_object_or_404(Post, pk=pk)
	return render(request, 'blog/post_detail.html', { 'post':post })

def post_new(request):
	if request.method == "POST":
		form = PostForm(request.POST)
		if form.is_valid():
			post = form.save(commit=False)
			post.author = request.user
			post.save()
			return redirect('blog.views.post_detail', pk=post.pk)
	else:
		form = PostForm()
	return render(request, 'blog/post_edit.html', {'form': form})

def post_edit(request, pk):
	post = get_object_or_404(Post, pk=pk)
	if request.method == "POST":
		form = PostForm(request.POST, instance=post)
		if form.is_valid():
			post = form.save(commit=False)
			post.author = request.user
			post.save()
			return redirect('blog.views.post_detail', pk=post.pk)
	else:
		form = PostForm(instance=post)
	return render(request, 'blog/post_edit.html', {'form': form})

# Create your views here.