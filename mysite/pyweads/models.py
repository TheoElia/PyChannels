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

class Product(models.Model):
    name = models.CharField(max_length=250, null=True,unique = True)
    price = models.IntegerField()
    product_img1 = models.ImageField(upload_to="accounts/static/pyweads/uploads", null=True, blank=True)
    product_img2 = models.ImageField(upload_to="accounts/static/pyweads/uploads", null=True, blank=True)
    product_img3 = models.ImageField(upload_to="accounts/static/pyweads/uploads", null=True, blank=True)
    img_name = models.CharField(max_length=250, null=True,unique = True)
    img_path = models.CharField(max_length=1000, null=True)
    img_download_url= models.TextField(null=True)
    description = models.TextField(null=True)
    reviewed = models.BooleanField(default=False)
    date_created = models.DateTimeField(default=django.utils.timezone.now)
    company = models.CharField(max_length=250, null=True)
    contact = models.CharField(max_length=14, null=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, on_delete = models.SET_NULL)


    class Meta:
        verbose_name = "Product"

    def __str__(self):
        return '%s' % (self.name)

    def image_tag(self):
        return mark_safe('<img src="{url}" width="{width}" height={height} "/>'.format(
            url = self.product_img1.url,
            width = 300,#obj.img.width,
            height=250,))#obj.img.height,))
    image_tag.short_description = 'Product Image'



