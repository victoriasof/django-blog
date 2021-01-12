from django.urls import path

from . import views

# You create the functions below (views.index views.post) inside blog/views.py
urlpatterns = [
    path('', views.index, name='index'),
    path('post/<int:post_id>', views.post, name='post'),
    path('add-post', views.add_post, name='add_post'),
]