from django.urls import path

from . import views

# You create the functions below (views.index views.post) inside blog/views.py
urlpatterns = [
    path('', views.index, name='index'),
    path('post/<int:post_id>', views.post, name='post'),
    path('add-post', views.add_post, name='add_post'),
    path('login', views.login_action, name='login'), # changed view name
    path('register', views.register, name='register'),
    path('logout', views.logout_action, name='logout'), # changed view name
    path('add-teacher-to-student', views.add_teacher_to_student, name='add_teacher_to_student'),
]
