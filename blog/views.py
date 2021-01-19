# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse, HttpResponseRedirect
from datetime import date
from random import randint
from django.urls import reverse
from django.contrib.auth import login, authenticate

from django.contrib.auth.models import User

from django.shortcuts import render
from .models import Post

# Create your views here.
def index(request): 
    #return HttpResponse('Index view') # Returns just a string as a response

    random_number = randint(1, 10)

    posts = Post.objects.all()

    # render function returns a HTML template
    # inside render i can pass variables for the view e.g name: 'Victoria'
    return render(request, 'index.html', {
        'name': 'Victoria',
        'age': 31,
        'random_number': random_number,
        'posts': posts
    })

def post(request, post_id):

    today = date.today()
    post = Post.objects.get(id=post_id)

    return render(request, 'post.html', {
        'title': 'Title', 
        'body': 'Body',
        'date_created': today.strftime('%d/%m/%Y'),
        'post': post
    })

def add_post(request):

    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('login'))
        
    # Check if user submitted a form with method = POST
    if request.method == 'POST':
        # Get POST data
        title = request.POST['title']
        content = request.POST['body']
        img_url = request.POST['imgUrl']

        newpost = Post(title=title, content=content, img_url=img_url)
        newpost.save()

    return render(request, 'add_post.html')


def login(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "login.html")
    else:
        return render(request, "login.html")

def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]

        user = User.objects.create_user(username, email, password)
        user.save()
        return HttpResponseRedirect(reverse('index'))

    return render(request, 'register.html')