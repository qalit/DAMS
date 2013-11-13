from DAMS.apps.blogs import models
from django.shortcuts import render_to_response, get_object_or_404
from DAMS.apps.blogs.models import Blog, Category

def index(request):
    return render_to_response('index.html', {
        'Categories': Category.objects.all(),
        'post': Blog.objects.all(),
    })

def view_post(request, slug):   
    return render_to_response('view_post.html', {
        'Post': get_object_or_404(Blog, slug=slug)
    })

def view_category(request, slug):
    category = get_object_or_404(Category, slug=slug)
    return render_to_response('view_category.html', {
        'Category': category,
        'posts': Blog.objects.filter(category=category)
    })