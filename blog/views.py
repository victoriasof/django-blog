# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from datetime import date
from random import randint

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

    # Check if user submitted a form with method = POST
    if request.method == 'POST':
        # Get POST data
        title = request.POST['title']
        content = request.POST['body']
        img_url = request.POST['imgUrl']

        newpost = Post(title=title, content=content, img_url=img_url)
        newpost.save()

    return render(request, 'add_post.html')