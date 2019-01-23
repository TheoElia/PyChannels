# -*- coding: utf-8 -*-
from __future__ import unicode_literals
# Register your models here.
from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group
from .models import File
from .forms import FileCreationForm,FileChangeForm
from django.conf import settings
from accounts.models import CustomUser
from django.utils.safestring import mark_safe
# Register your models here.

class FileAdmin(admin.ModelAdmin):
    add_form = FileCreationForm
    form = FileChangeForm
    model = File
    fields = ['image_tag', 'firebase_path','file_path','name','download_url','user']
    readonly_fields = ['image_tag','firebase_path','file_path','name','download_url','user']

    def image_tag(self, obj):
        return mark_safe('<img src="{url}" width="{width}" height={height} />'.format(
            url = obj.download_url,
            width = 300,#obj.img.width,
            height=250,))#obj.img.height,))
    image_tag.short_description = 'Image'
    
    ## Defines the list of fields displayed on admin page
    list_display = ['firebase_path','file_path','name','download_url', 'date_created','user']
                    #'password', 'date_joined','phone','email_confirmed','admin_name']
    # Enables editing other fields
    #fieldsets = UserAdmin.fieldsets + (
     #   ('Extra Fields', {'fields': ('phone',)}),
    #)

    def is_member(self,user_id,group_name):
        user = CustomUser.objects.get(pk=user_id)
        return user.groups.filter(name=group_name).exists()

    def get_queryset(self, request):
        if request.user.is_superuser:
            return File.objects.all()
        if request.user.is_staff and self.is_member(request.user.id, 'Patrons'):
            #print(Retailer.objects.filter(admin=request.user.id))
            return File.objects.filter(user=request.user)
        if request.user.is_staff and self.is_member(request.user.id, 'Retailers'):
            #print(Retailer.objects.filter(admin=request.user.id))
            return File.objects.filter(user=request.user)
        return None

    #def has_change_permission(self, request, obj=None):
     #   has_class_permission = super(SmsAdmin, self).has_change_permission(request, obj)
      #  if not has_class_permission:
       #     return False
        #if obj is not None and not request.user.is_superuser and request.user != obj.user:
         #   return False
        #return True
    def has_change_permission(self, request, obj=None):
        if obj is not None and obj.user != request.user and not request.user.is_superuser and not request.user.is_staff:
            return False
        return True

    def has_delete_permission(self, request, obj=None):
        if obj is not None and obj.user != request.user and not request.user.is_superuser and not request.user.is_staff:
            return False
        return True
    def has_create_permission(self, request, obj=None):
        if obj is not None and obj.user != request.user and not request.user.is_superuser and not request.user.is_staff:
            return False
        return True
    def save_model(self, request, obj, form, change):
        if not obj.user:
            obj.user = request.user
        obj.save()


admin.site.register(File,FileAdmin)#, SmsAdmin)

