from django.shortcuts import render
from django.contrib.auth.models import Group
from django.core.mail import send_mail
from django.core.mail import EmailMultiAlternatives
# Create your views here.
from django.shortcuts import render, redirect,HttpResponse,HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView
from django.contrib.auth.models import Group, User
from django.contrib.auth import authenticate,login,logout
from django.views.generic import View
from tastypie.models import ApiKey
from django.db import models
from .forms import ProductCreationForm,ProductChangeForm
from django.contrib.auth import views
from tastypie.models import create_api_key
import os
import binascii
from django.template.loader import render_to_string
from django.contrib import messages
from django.shortcuts import get_object_or_404
from django.views.generic import ListView
from .models import Product
from django.utils.safestring import mark_safe
from django.views.generic.detail import DetailView
from django.utils import timezone


class CreateProductView(TemplateView):
    form_class = ProductCreationForm
    success_url = reverse_lazy('home')
    template_name = 'pyweads/product_creation.html'

    def get(self, request):
        form = self.form_class
        args = {'form': form,"warning":"Your product will be reviewed and posted on our page."}
        return render(request,self.template_name,args)

    def post(self,request):
        form = self.form_class(request.POST)
        if form.is_valid():
            group = Group.objects.get(name='Patrons')
            name = form.cleaned_data['name']
            price = form.cleaned_data['price']
            description = form.cleaned_data['description']
            product = self.form_valid(form)
            product.user = request.user
            product.product_img1 = request.FILES['product_img1']
            product.product_img2 = request.FILES['product_img2']
            product.product_img3 = request.FILES['product_img3']
            product.save()
            messages.success(request, "You have succefully added a product. Thanks")
            return redirect('create_product')

        args = {'form': form,"warning":"Your product will be reviewed and posted"}
        return render(request, self.template_name, args)




    def create_group(group_name):
        group = Group(name=group_name)
        group.save()

    def add_user_to_group(group_name,user_id):
        group = Group.objects.get(name=group_name)
        #users = CustomUser.objects.all()
        user = CustomUser.objects.get(pk=user_id)
        user.groups.add(group)        # user is now in the "group_name" group

    def is_member(self,user_id,group_name):
        user = CustomUser.objects.get(pk=user_id)
        return user.groups.filter(name=group_name).exists()

    def is_in_multiple_groups(user_id,list_of_groups):
        user = CustomUser.objects.get(pk=user_id)
        return user.groups.filter(name__in=list_of_groups).exists()

    def form_valid(self, form):
        user = form.save()
        return user
    def get_context_data(self, **kwargs):
        context = super(CreatePatronView, self).get_context_data(**kwargs)
        context.update({'success': "We have sent you an email. Check for your secret key."})
        return context


#def lessons(request):
 #   template_name = 'lessons.html'
  #  objs = Lesson.objects.filter(reviewed = False)
   # args = {'objs':objs}
    #return render(request,template_name, args)


def email_verification(request, email_token):
    form_class = PatronCreationForm
    success_url = reverse_lazy('home')
    template_name = 'signup.html'
    form = form_class
    args = {'form': form,"warning":"You provided a wrong token"}
    try:
        user = Patron.objects.get(email_token=email_token)
    except:
        return render(request, template_name, args)
    else:
        user.email_confirmed = 1
        user.is_active = True
        user.is_staff = True
        user.save()#user = authenticate(username=user.username, password=user.password)
        login(request, user)
        return redirect('home')#HttpResponse(user)

def email_us(request):
    message = request.POST['message']
    email = request.POST['email']
    name = request.POST['name']
    subject = "Email from {}".format(name)
    try:
        send_mail(subject,message+" From {}".format(email),'pythonwithellie@gmail.com',["theophylusnhutiphapha@gmail.com"],fail_silently=False,)
    except:
        messages.success(request, "Hi {}, There was a problem sending your message".format(name))
        return redirect('home')
    else:
        messages.success(request, "Hi {}, Your message has been sent to the team.".format(name))
        return redirect('home')

class ProductListView(ListView):
    model = Product
    def get_context_data(self, **kwargs):
        context = super(ProductListView, self).get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context

    def get_queryset(self):
            return Product.objects.filter(reviewed=True)


class ProductDetailView(DetailView):
    model = Product
    def get_context_data(self, **kwargs):
        context = super(ProductDetailView, self).get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context

    def get_queryset(self):
            return Product.objects.filter(reviewed=True)








