from django.contrib import admin
# Register your models here.
from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group
from tastypie.models import ApiKey

from .forms import CustomUserCreationForm, CustomUserChangeForm,PatronCreationForm,PatronChangeForm,RetailerCreationForm,RetailerChangeForm
from .models import CustomUser, Patron,Retailer
from django.utils.safestring import mark_safe


def make_superuser(modeladmin, request, queryset):
    queryset.update(is_superuser=True)
make_superuser.short_description = "Mark selected users as superusers"

def make_staff(modeladmin, request, queryset):
    queryset.update(is_staff=True)
make_staff.short_description = "Mark selected users as staffs"

def unmake_superuser(modeladmin, request, queryset):
    queryset.update(is_superuser=False)
unmake_superuser.short_description = "Unmark selected users as superusers"

def unmake_staff(modeladmin, request, queryset):
    queryset.update(is_staff=False)
unmake_staff.short_description = "Unmark selected users as staffs"

def make_active(modeladmin, request, queryset):
    queryset.update(is_active=True)
make_active.short_description = "Mark selected users as active"

def make_inactive(modeladmin, request, queryset):
    queryset.update(is_active=False)
make_inactive.short_description = "Mark selected users as inactive"




class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    # Defines the list of fields displayed on admin page
    list_display = ['username','email', 'date_joined','reset_token','is_patron','last_login','is_active',]
    #fields = ['username','email',  'password', 'date_joined', 'image_tag', 'user_img','reset_token','is_patron','last_login','is_active','is_staff']
    readonly_fields = ['image_tag',]
    # Enables editing other fields

    fieldsets = UserAdmin.fieldsets + (
       ('Extra Fields', {'fields': ('user_img',)}),
    )

    actions = [make_superuser, make_staff, unmake_superuser, unmake_staff, make_active, make_inactive]

    def image_tag(self, obj):

        return mark_safe('<img src="{url}" width="{width}" height={height} "/>'.format(
            url = obj.user_img.url,
            width = 300,#obj.img.width,
            height=250,))#obj.img.height,))
    image_tag.short_description = 'User Image'





class PatronAdmin(admin.ModelAdmin):
    add_form = PatronCreationForm
    form = PatronChangeForm
    model = Patron

    ## Defines the list of fields displayed on admin page
    list_display = ['username', 'email', 'date_joined','email_confirmed','last_login','email_token']
    # Enables editing other fields
    fields = ('username','email','password')
    #fieldsets = UserAdmin.fieldsets + (
     #   ('Extra Fields', {'fields': ('phone','is_patron',)}),
    #)
    #exclude = ['is_superuser',]

    def image_tag(self, obj):

        return mark_safe('<img src="{url}" width="{width}" height={height} "/>'.format(
            url = obj.user_img.url,
            width = 300,#obj.img.width,
            height=250,))#obj.img.height,))
    image_tag.short_description = 'User Image'

    def is_member(self,user_id,group_name):
        user = CustomUser.objects.get(pk=user_id)
        return user.groups.filter(name=group_name).exists()

    def get_queryset(self, request):
        if request.user.is_superuser:
            return Patron.objects.all()
        if self.is_member(request.user.id, 'Patrons'):
            #print(Retailer.objects.filter(admin=request.user.id))
            return Patron.objects.filter(id=request.user.id)
        return None

    def has_change_permission(self, request, obj=None):
        has_class_permission = super(PatronAdmin, self).has_change_permission(request, obj)
        if not has_class_permission:
            return False
        if obj is not None and not request.user.is_superuser and request.user.id != obj.id:
            return False
        return True


class RetailerAdmin(admin.ModelAdmin):
    add_form = RetailerCreationForm
    form = RetailerChangeForm
    model = Retailer
    ## Defines the list of fields displayed on admin page
    list_display = ['username', 'first_name', 'last_name','email',
                    'password', 'date_joined','phone','email_confirmed','admin_name']
    # Enables editing other fields
    fields = ('username', 'first_name', 'last_name','email','phone','password',)
    #fieldsets = UserAdmin.fieldsets + (
     #   ('Extra Fields', {'fields': ('phone',)}),
    #s)

    def is_member(self,user_id,group_name):
        user = CustomUser.objects.get(pk=user_id)
        return user.groups.filter(name=group_name).exists()

    def get_queryset(self, request):
        if request.user.is_superuser:
            return Retailer.objects.all()
        if self.is_member(request.user.id, 'Retailers'):
            #print(Retailer.objects.filter(admin=request.user.id))
            return Retailer.objects.filter(id=request.user.id)

        if self.is_member(request.user.id, 'Patrons'):
            #print(Retailer.objects.filter(admin=request.user.id))
            return Retailer.objects.filter(admin=request.user.id)
        return None

    def has_change_permission(self, request, obj=None):
        has_class_permission = super(RetailerAdmin, self).has_change_permission(request, obj)
        if not has_class_permission:
            return False
        if obj is not None and not request.user.is_superuser and request.user != obj and not request.user.id == obj.admin:
            return False
        return True



admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Patron, PatronAdmin)
#admin.site.register(Retailer, RetailerAdmin)
