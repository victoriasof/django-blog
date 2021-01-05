# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from datetime import date
from random import randint

from django.shortcuts import render

# Create your views here.
def index(request): 
    #return HttpResponse('Index view') # Returns just a string as a response

    random_number = randint(1, 10)

    # render function returns a HTML template
    # inside render i can pass variables for the view e.g name: 'Victoria'
    return render(request, 'index.html', {
        'name': 'Victoria',
        'age': 31,
        'random_number': random_number
    })

def post(request):

    return render(request, 'post.html', {
        'title': 'Title', 
        'body': 'Body',
        'date_created': date(2020, 1, 5).strftime('%d/%m/%Y')
    })

def add_post(request):

    # Check if user submitted a form with method = POST
    if request.method == 'POST':
        # Get POST data
        title = request.POST['title']
        content = request.POST['body']
        #print(title)
        #print(content)

    return render(request, 'add_post.html')