# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse, HttpResponseRedirect
from datetime import date
from random import randint
from django.urls import reverse
from django.contrib.auth import login, authenticate, logout

from django.contrib.auth.models import User

from django.shortcuts import render
from .models import Post, Student, Teacher

# Create your views here.
def index(request):
    print(request.user) # Added just to check logged in user
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

# added
# if i add login in the fuctions name i get conflict with the builtin login function
def login_action(request):
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
        login(request, user)
        return HttpResponseRedirect(reverse('index'))

    return render(request, 'register.html')

# Added
# if i write logout i get conflict with the built in logout function
def logout_action(request):
    logout(request)
    return HttpResponseRedirect(reverse('login'))

def add_teacher_to_student(request):
    if request.method == 'POST':
        studentId = request.POST['studentId']
        teacherId = request.POST['teacherId']

        s = Student.objects.get(id=studentId)
        t = Teacher.objects.get(id=teacherId)

        s.teachers.add(t)
        s.save()

    students = Student.objects.all()
    teachers = Teacher.objects.all()

    # return render(request, 'movies/movie.html', {
    #     'actors': [{
    #         'name': actor.name,
    #         'bio': actor.bio,
    #         'photos': actor.photos.all()
    #     } for actor in actors],
    # })

    return render(request, 'add_teacher.html', {
        'students': students,
        'teachers': teachers
    })
