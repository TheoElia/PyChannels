# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
from django.db import models
import django
from datetime import datetime
# from django.contrib.auth.models import User
from django.db import models
from tastypie.models import create_api_key
from django.conf import settings
from django_mysql.models import ListCharField
from django_mysql.models import ListTextField
from django.utils.safestring import mark_safe
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from froala_editor.fields import FroalaField
import random


# Create your models here.
STATUS_CHOICES = (('d', 'Draft'),('p', 'Published'),('w', 'Withdrawn'),)
class Lesson(models.Model):

    title = models.CharField(max_length=250, null=True,unique = True)
    #sub_topics = ListTextField(base_field=models.CharField(max_length=1000),size=5000,blank=True)
    intro_text = models.CharField(max_length=1000, null=True,unique = False)
    lesson_img = models.ImageField(upload_to="accounts/static/lessons/uploads", null=True, blank=True)
    img_name = models.CharField(max_length=250, null=True,unique = True)
    img_path = models.CharField(max_length=1000, null=True)
    img_download_url= models.TextField(null=True)
    body = models.TextField(null=True)#FroalaField()
    reviewed = models.BooleanField(default=False)
    date_created = models.DateTimeField(default=django.utils.timezone.now)
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default='d')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank = True, on_delete = models.SET_NULL)






    class Meta:
        verbose_name = "Lesson"

    def __str__(self):
        return '%s' % (self.title)

    def image_tag(self):
        return mark_safe('<img src="{url}" width="{width}" height={height} "/>'.format(
            url = self.lesson_img.url,
            width = 300,#obj.img.width,
            height=250,))#obj.img.height,))
    image_tag.short_description = 'Lesson Image'

class Comment(models.Model):
    #first_words = models.CharField(max_length=250, null=True)
    comment = models.TextField(null=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank = True, on_delete = models.SET_NULL)
    module = models.ForeignKey(Lesson, null=True, blank = True, on_delete = models.SET_NULL)
    date_created = models.DateTimeField(default=django.utils.timezone.now)



    def __str__(self):
        return '%s' % (self.comment)

class Image(models.Model):
    image = models.ImageField(upload_to="accounts/static/lessons/uploads")
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey("content_type", "object_id")


class Trick(models.Model):
    description = models.TextField(null=True)
    code = models.TextField(null=True)
    date_created = date_created = models.DateField(default=django.utils.timezone.now)

    def __str__(self):
        des_list = self.description.split(" ")
        return '%s' % (des_list[0])

class Robot(models.Model):
    message = models.TextField(null=True)
    response = models.TextField(null=True)
    category = models.CharField(max_length=1000, null=True,unique = False)