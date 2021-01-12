# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField(max_length=200)
    img_url = models.URLField()
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.id} - {self.content} - created at: {self.created_at}'

