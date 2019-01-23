# -*- coding: utf-8 -*-
from __future__ import unicode_literals
# Register your models here.
from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group
from .models import Product
from .forms import ProductCreationForm,ProductChangeForm
from django.conf import settings
from accounts.models import CustomUser
from django.utils.safestring import mark_safe
# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    add_form = ProductCreationForm
    form = ProductChangeForm
    model = Product
    fields = ['name','price','image_tag','description','img_name', 'reviewed','product_img1','product_img2','product_img3','user','company','contact']
    readonly_fields = ['image_tag','img_name','img_path','img_download_url','user']

    def image_tag(self, obj):

        return mark_safe('<img src="{url}" width="{width}" height={height} "/>'.format(
            url = obj.product_img1.url,
            width = 300,#obj.img.width,
            height=250,))#obj.img.height,))
    image_tag.short_description = 'Product Image'

    ## Defines the list of fields displayed on admin page
    list_display = ['name','price','description','img_name', 'date_created','reviewed','user']
                    #'password', 'date_joined','phone','email_confirmed','admin_name']
    # Enables editing other fields
    #fieldsets = ProductAdmin.fieldsets + (
    #    ('Extra Fields', {'fields': ('contact','company',)}),
    #)

    def is_member(self,user_id,group_name):
        user = CustomUser.objects.get(pk=user_id)
        return user.groups.filter(name=group_name).exists()

    def get_queryset(self, request):
        if request.user.is_superuser:
            return Product.objects.all()
        if request.user.is_staff and self.is_member(request.user.id, 'Patrons'):
            #print(Retailer.objects.filter(admin=request.user.id))
            return Product.objects.filter(user=request.user)
        if request.user.is_staff and self.is_member(request.user.id, 'Retailers'):
            #print(Retailer.objects.filter(admin=request.user.id))
            return Product.objects.filter(user=request.user)
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


admin.site.register(Product,ProductAdmin)#, SmsAdmin)

