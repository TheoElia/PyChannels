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


# Create your models here.

class File(models.Model):
    name = models.CharField(max_length=250, null=True,unique = True)
    firebase_path = models.CharField(max_length=250, null=True,unique = True)
    file_path = models.CharField(max_length=1000, null=True)
    img = models.ImageField(upload_to="images", null=True, blank=True)
    download_url = models.TextField(null=True)
    date_created = models.DateTimeField(default=django.utils.timezone.now)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, null=True)
    

    class Meta:
        verbose_name = "File"

    def __str__(self):
        return '%s' % (self.name)
    

    #def image_tag(self):
     #   return mark_safe('<img src="/home/theoelia/PycharmProjects/myproject/intelliapi/images/%s" width="150" height="150" />' % (self.name))

    #image_tag.short_description = 'Img'


#models.signals.post_save.connect(create_api_key, sender=User)
