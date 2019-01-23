from random import choice
from django.contrib.auth.models import AbstractUser
from django.db import models
import django
from werkzeug.security import generate_password_hash
from datetime import datetime
from django.contrib.auth.models import User
from django.conf import settings
from tastypie.models import create_api_key
from django.utils.safestring import mark_safe


# Create your models here.
class CustomUser(AbstractUser):
    # add additional fields in here
    email = models.EmailField(blank=False)
    is_staff = models.BooleanField( default=True)
    date_joined = models.DateTimeField(default=django.utils.timezone.now())
    reset_token = models.CharField(max_length=1000,default=generate_password_hash(str(datetime.now())))
    is_patron = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    last_activity = models.DateTimeField(default=django.utils.timezone.now())
    user_img = models.ImageField(upload_to="accounts/static/accounts/uploads", null=True, blank=True)

    def __str__(self):
        return self.username

    def get_absolute_url(self):
        # return reverse('accounts.views.user-details', args=[str(self.id)])
        return "/accounts/user/%i/" % self.id

    def image_tag(self):
        return mark_safe('<img src="{url}" width="{width}" height={height} "/>'.format(
            url = self.user_img.url,
            width = 300,#obj.img.width,
            height=250,))#obj.img.height,))
    image_tag.short_description = 'User Image'



class Patron(CustomUser):
    # add additional fields ail_in here
    #phone = models.CharField(max_length=14, blank=False, unique=True)
    #date_joined = models.DateTimeField(default=django.utils.timezone.now())
    #user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    #phone = models.CharField(max_length=14, blank=False, unique=True)
    email_token = models.CharField(max_length=1000,default=generate_password_hash(str(datetime.now())))
    email_confirmed = models.IntegerField(default=0)

    class Meta:
        verbose_name = "Patron"

    def __str__(self):
        return self.username



class Retailer(CustomUser):
    # add additional fields ail_in here
    #phone = models.CharField(max_length=14, blank=False, unique=True)
    #date_joined = models.DateTimeField(default=django.utils.timezone.now())
    #user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    phone = models.CharField(max_length=14, blank=False)
    email_token = models.CharField(max_length=1000,default=generate_password_hash(str(datetime.now())))
    email_confirmed = models.IntegerField(default=0)
    admin = models.IntegerField(default=1)
    admin_name = models.CharField(max_length=200,default='')

    #is_staff = models.BooleanField( default=False)

    class Meta:
        verbose_name = "Retailer"

    def __str__(self):
        return self.username


def set_token(self):
        self.token = ''.join([choice('abcdefghijklmnopqrstuvwxyz0123456789') for i in range(15)])
        return self.token





