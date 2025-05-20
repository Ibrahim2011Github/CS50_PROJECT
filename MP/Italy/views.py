from django.shortcuts import render, redirect
from .models import *
from django.http import HttpResponse
from django.conf.urls.static import static
# Create your views here.

menu = [{'title': "About", 'url_name': "about"},
        {'title': "Categories", 'url_name': "add_page"},
        {'title': "Contact", 'url_name': "contact"},
        {'title': "Enter", 'url_name': "login" }] 

def index(request):
    posts = Italy.objects.all()
    context = {
        "title": 'Home',
        "posts": posts,
        # "cats" : cats,
        "menu": menu,
        # "cat_selected": 0,
    }
    return render(request, 'Italy/index.html', context=context)

def about(request):
    posts = Italy.objects.all()
    context = {
        "title": 'About',
        "posts": posts,
        # "cats" : cats,
        "menu": menu,
        # "cat_selected": 0,
    }
    return render(request, 'Italy/about.html', context=context)

def base(request):
    return render(request, 'Italybase.html', {'menu': menu, 'title': 'About'})


def show_post(request, post_id):
    posts = Italy.objects.all()
    post = Italy.objects.get(pk=post_id)
    context = {
        'post_id': post_id,
        "title": 'About',
        "posts": posts,
        # "cats" : cats,
        "menu": menu,
        # "cat_selected": 0,
    }
    return render(request, 'Italy/post.html', context=context)



