from django.shortcuts import render
from .forms import *
from .models import *


# Create your views here.
def welcome(request):
    context = {'message': "Hello there I am sonia"}
    return render(request, 'index.html', context)

def blog_list(request):
    blogs = Blog.objects.all()
    context = {'blogs': blogs}
    return render(request, 'blog_list.html', context)

def add_blog(request):
    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES)
        if form.is_valid():
            blog = form.save()
            blog.save()
    else:
        form = BlogForm
    return render(request, 'add_blog.html', {'form': form})


