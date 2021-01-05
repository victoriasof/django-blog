## How to create Django app

1. use django-admin to create project -> django-admin startproject myproject
2. create app -> python3 manage.py startapp blog
3. register app in settings.pys // settings.py line 40
4. in main urls.py import path and include -> from django.urls import include, path
5. convert admin route to this -> path('admin/', admin.site.urls),
6. create urls.py inside my new app (blog) // copy the code from the docs
7. import the newly created blog/urls.py inside the main urls.py using the include() function
8. create the views that you declared inside the urls.py in your app folder
9. run the command python3 manage.py migrate (creates some default Django settings inside your database)
10. python3 manage.py runserver to run a development server and check our code