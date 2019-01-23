# -*- coding: utf-8 -*-
from __future__ import unicode_literals
# Register your models here.
from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group
from .models import Lesson
from .forms import LessonCreationForm,LessonChangeForm
from django.conf import settings
from accounts.models import CustomUser
from django.utils.safestring import mark_safe
from django.contrib import admin
from django.contrib.contenttypes.admin import GenericTabularInline
from .models import Image, Lesson
class ImageInline(GenericTabularInline):
    model = Image



# Register your models here.
def make_published(LessonAdmin, request, queryset):
    queryset.update(status='p')
make_published.short_description = "Mark selected lessons as published"

def make_withdrawn(LessonAdmin, request, queryset):
    queryset.update(status='w')
make_withdrawn.short_description = "Mark selected lessons as withdrawn"

def make_reviewed(LessonAdmin, request, queryset):
    queryset.update(reviewed=True)
make_reviewed.short_description = "Mark selected lessons as reviewed"


class LessonAdmin(admin.ModelAdmin):

    add_form = LessonCreationForm
    form = LessonChangeForm
    model = Lesson
    fields = ['title','intro_text','image_tag','body', 'reviewed','status','lesson_img','user',]
    readonly_fields = ['image_tag',]
    actions = [make_published,make_reviewed,make_withdrawn]



    def image_tag(self, obj):

        return mark_safe('<img src="{url}" width="{width}" height={height} "/>'.format(
            url = obj.lesson_img.url,
            width = 300,#obj.img.width,
            height=250,))#obj.img.height,))
    image_tag.short_description = 'Lesson Image'

    ## Defines the list of fields displayed on admin page
    list_display = ['title','intro_text', 'date_created','reviewed','status','user']
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
            return Lesson.objects.all()
        if request.user.is_staff and self.is_member(request.user.id, 'Patrons'):
            #print(Retailer.objects.filter(admin=request.user.id))
            return Lesson.objects.filter(user=request.user)
        if request.user.is_staff and self.is_member(request.user.id, 'Retailers'):
            #print(Retailer.objects.filter(admin=request.user.id))
            return Lesson.objects.filter(user=request.user)
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



admin.site.register(Lesson,LessonAdmin)#, SmsAdmin)

