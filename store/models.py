# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from django.contrib.auth.models import User
from django.core.validators import URLValidator
import datetime

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=140)

    def __unicode__(self):
        return self.name


class Product(models.Model):
    title = models.CharField(max_length=250)
    description = models.TextField()
    timestamp = models.DateTimeField(auto_now=True)
    date = models.DateField(default=datetime.date.today)
    company = models.ForeignKey(User, null=True)
    location = models.CharField(max_length=400, blank=True, null=True)
    code = models.CharField(max_length=250, blank=True, null=True)
    category = models.ForeignKey(Category, null=True)
    link = models.TextField(validators=[URLValidator()], blank=True, null=True)
    image_url = models.TextField(validators=[URLValidator()],
        blank=True, null=True)

    def __unicode__(self):
        return self.title
