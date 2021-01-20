# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import Post, Review, Teacher, Student

# Register your models here.
admin.site.register(Post)
admin.site.register(Review)
admin.site.register(Teacher)
admin.site.register(Student)