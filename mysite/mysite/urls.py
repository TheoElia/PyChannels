"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls import url, include
from django.views.generic.base import TemplateView
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
#from pywefirebase.resources import FileResource
from lessons.resources import LessonResource
from accounts import views

#file_resource = FileResource()
lesson_resource = LessonResource()

urlpatterns = [
    #url(r'^$', TemplateView.as_view(template_name='para.html'), name='home'),
    #url(r'^$', views.UserListView.as_view(template_name="accounts/para.html"), name='home'),

    url(r'^admin/', admin.site.urls),
url(r'^chat/', include('chat.urls')),
    url('accounts/', include('django.contrib.auth.urls')),
    url('accounts/', include('accounts.urls')),
    url('lessons/', include('lessons.urls')),
    url('products/', include('pyweads.urls')),
    url(r'^lessonapi/', include(lesson_resource.urls)),
    #url(r'^fireapi/', include(file_resource.urls)),
    url(r'^froala_editor/', include('froala_editor.urls')),
    url(r'^$', include('accounts.urls')),
    url(r'^',  include('lessons.urls')),



    #url('api/', include('smsapi.urls')),
    #url(r'^api-auth/', include('rest_framework.urls'))

]
urlpatterns+= staticfiles_urlpatterns()
