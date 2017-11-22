# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.db import models

from django.contrib.auth.models import User
from django.core.validators import URLValidator


# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=140)


class Product(models.Model):
    title = models.CharField(max_length=250)
    description = models.TextField()
    date = models.TextField()
    company = models.ForeignKey(User, null=True)
    location = models.CharField(max_length=400)
    code = models.CharField(max_length=250)
    category = models.ForeignKey(Category, null=True)
    image_url = models.TextField(validators=[URLValidator()], blank=True,
                                 null=True)
