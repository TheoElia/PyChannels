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
from accounts.models import CustomUser
from .forms import LessonCreationForm,LessonChangeForm,CommentCreationForm
from django.contrib.auth import views
from tastypie.models import create_api_key
import os
import binascii
from django.template.loader import render_to_string
from django.contrib import messages
from django.shortcuts import get_object_or_404
from django.views.generic import ListView
from .models import Lesson,Comment,Trick
from pyweads.models import Product
from django.utils.safestring import mark_safe
from django.views.generic.detail import DetailView
from django.utils import timezone
import online_users.models
from datetime import datetime, timedelta
from weasyprint import HTML, CSS
from django.conf import settings
import tempfile
import requests as r






class CreateLessonView(TemplateView):
    form_class = LessonCreationForm
    success_url = reverse_lazy('home')
    template_name = 'lessons/lesson_creation.html'

    def get(self, request):
        form = self.form_class
        args = {'form': form,"warning":"Your lesson will be reviewed and posted on our page."}
        return render(request,self.template_name,args)

    def post(self,request):
        form = self.form_class(request.POST)
        if form.is_valid():
            group = Group.objects.get(name='Patrons')
            #title = form.cleaned_data['title']
            #intro_text = form.cleaned_data['intro_text']
            body = form.cleaned_data['body']
            lesson = self.form_valid(form)
            lesson.user = request.user
            lesson.body = str(body)
            try:
                lesson.lesson_img = request.FILES['lesson_img']
            except Exception as e:
                messages.success(request, "Please add an image")
                return redirect('create_lesson')
            else:
                lesson.save()
                messages.success(request, "You have succefully added a lesson. Thanks")
                return redirect('create_lesson')
        else:
            messages.success(request, "There was an error, make sure all fields are filled and image is attached.")
            return redirect('create_lesson')
        args = {'form': form,"warning":"There was an error, make sure all fields are filled and image is attached."}
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
        obj = form.save(commit=False)
        obj.user = self.request.user
        obj.save
        return obj

    def get_context_data(self, **kwargs):
        context = super(CreateLessonView, self).get_context_data(**kwargs)
        context.update({'success': "We have sent you an email. Check for your secret key."})
        return context


class CreateCommentView(TemplateView):
    form_class = CommentCreationForm
    success_url = reverse_lazy('home')
    template_name = 'lessons/lesson_creation.html'

    def get(self, request):
        form = self.form_class
        args = {'form': form,"warning":"Your lesson will be reviewed and posted on our page."}
        return render(request,self.template_name,args)

    def post(self,request):
        form = self.form_class(request.POST)
        if form.is_valid():
            #group = Group.objects.get(name='Patrons')
            #title = form.cleaned_data['title']
            #intro_text = form.cleaned_data['intro_text']
            comment_body = form.cleaned_data['comment']
            module = form.cleaned_data['module']
            module = Lesson.objects.get(title=str(module))
            comment = self.form_valid(form)
            comment.user = request.user
            comment.comment = comment_body
            #comment.module = module
            comment.save()
            messages.success(request, "You have succefully added a lesson. Thanks")
            return redirect('/lessons/lesson/{}'.format(module.id))
        args = {'form': form,"warning":"There was an error, make sure all fields are filled and image is attached."}
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
        obj = form.save(commit=False)
        obj.user = self.request.user
        #obj.save
        return obj

    def get_context_data(self, **kwargs):
        context = super(CreateLessonView, self).get_context_data(**kwargs)
        context.update({'success': "We have sent you an email. Check for your secret key."})
        return context

from django.utils.timezone import utc



class LessonListView(ListView):
    model = Lesson
    def get_context_data(self, **kwargs):
        users_list = []
        context = super(LessonListView, self).get_context_data(**kwargs)
        context['now'] = timezone.now()
        all_users = CustomUser.objects.all()
        for user in all_users:
            if get_time_diff(user) < 60:
                users_list.append(user)
                #users_list.append(get_time_diff(user))
        if self.request.user in users_list:
            context['online_users'] = users_list.remove(self.request.user)
        else:
             context['online_users'] = users_list
        context['number_online'] = len(users_list)

        context['product_list'] = Product.objects.filter(reviewed=True)
        sms_list1 = []
        sms_list2 = []
        sms_list3 = []
        lesson_list = Lesson.objects.all()
        for each in lesson_list:
            if len(sms_list1) <= 10:
                sms_list1.append(each)
            elif len(sms_list2) <= 10:
                sms_list2.append(each)
            else:
                sms_list3.append(each)
        context['lesson_list'] = lesson_list
        context['lesson_list1'] = sms_list1
        context['lesson_list2'] = sms_list2
        context['lesson_list3'] = sms_list3
        context['object'] = Lesson.objects.filter(status="p")[0]
        yesterday = (datetime.now() - timedelta(1)).date()
        today = datetime.today().date()
        tricks = Trick.objects.order_by('date_created')
        #if len(tricks) < 1:
        #    tricks = Trick.objects.all()
        if len(tricks) != 0:
            context['trick'] = tricks[len(tricks)-1]
        return context
    def get_queryset(self):
            return Lesson.objects.filter(status="p")

def get_time_diff(user):
    if user.last_activity:
        now = datetime.utcnow().replace(tzinfo=utc)
        timediff = now - user.last_activity
        return timediff.total_seconds()


class LessonDetailView(DetailView):
    model = Lesson
    def get_context_data(self, **kwargs):
        from random import sample
        people_ymk = []
        context = super(LessonDetailView, self).get_context_data(**kwargs)
        context['now'] = timezone.now()
        my_list = Product.objects.filter(reviewed=True)[::-1]
        my_list2 = Product.objects.filter(reviewed=True).order_by('date_created')[:]
        if self.object.id < 25:
            context['next'] = self.object.id+1
        else:
            context['next'] = 1
        if self.object.id > 1:
            context['prev'] = self.object.id-1
        else:
            context['prev'] = 25
        context['products'] = my_list2
        context['products2'] = my_list
        context['comments'] = Comment.objects.filter(module=self.object)

        if self.request.user.is_authenticated:
            #friends = self.request.user.friends.all()
            #context['friends'] = friends.exclude(id=(self.request.user.id))
            people = CustomUser.objects.exclude(id=(self.request.user.id))
            #for i in people:
            #    if i not in friends:
            #        if i not in people_ymk:
            #            people_ymk.append(i)
            #context['users'] = sample(people_ymk,10)
        yesterday = (datetime.now() - timedelta(1)).date()
        today = datetime.today().date()
        tricks = Trick.objects.order_by('date_created')
        #if len(tricks) < 1:
        #    tricks = Trick.objects.all()
        if len(tricks) != 0:
            context['trick'] = tricks[len(tricks)-1]
        context['object_list'] = Lesson.objects.filter(status="p").exclude(id=self.object.id)
        return context

    def get_queryset(self):
            return Lesson.objects.filter(status="p")

def lesson_tryit(request):
    template_name = 'lessons/slider.html'
    return render(request, template_name)

def next_lesson(request,num):
    template_name = "lessons/lesson_list.html"
    template_name2 = "lessons/lesson_list2.html"
    template_name3 = "lessons/lesson_list3.html"
    lesson_list = Lesson.objects.all()
    sms_list1 =[]
    sms_list2 = []
    sms_list3 = []
    for each in lesson_list:
        if len(sms_list1) < 10:
            sms_list1.append(each)
        elif len(sms_list2) < 10:
            sms_list2.append(each)
        else:
            sms_list3.append(each)
    if int(num) == 2:
        args = {'lesson_list2':sms_list2,'all':len(lesson_list)}
        return render(request,template_name2,args)
    else:
        args = {'lesson_list3':sms_list3,'list2':len(sms_list2),'all':len(lesson_list)}
        return render(request,template_name3,args)
    return render(request,template_name)


def redirect_lesson(request,title):
    try:
        lesson = Lesson.objects.get(title=title)
    except:
        return redirect('/lessons')
    else:
        pk = lesson.id
        return redirect("/lessons/lesson/{}/".format(pk))

def add_friend(request,friend_id,lesson_id):
    user = CustomUser.objects.get(id=request.user.id)
    friend = CustomUser.objects.get(id=friend_id)
    user.friends.add(friend)
    user.save()
    messages.success(request,"Friend added")
    return redirect('/lessons/lesson/{}/'.format(lesson_id))


def remove_friend(request,friend_id,lesson_id):
    user = CustomUser.objects.get(id=request.user.id)
    friend = CustomUser.objects.get(id=friend_id)
    user.friends.remove(friend)
    user.save()
    messages.success(request,"Friend removed")

    return redirect('/lessons/lesson/{}/'.format(lesson_id))

def create_comment(request):
    comment = request.POST['comment']
    module = request.POST['module']
    module = Lesson.objects.get(title=module )
    com = Comment(comment=comment,user=request.user,module=module)
    com.save()
    return redirect('/lessons/lesson/{}/'.format(module.id))

def del_comment(request,comment_id,lesson_id):
    comment = Comment.objects.get(id=comment_id)
    if request.user == comment.user:
        comment.delete()
        messages.success(request, "Comment deleted!")
        return redirect('/lessons/lesson/{}/'.format(lesson_id))
    messages.error(request, "You cannot delete this comment!")
    return redirect('/lessons/lesson/{}/'.format(lesson_id))

def generate_pdf(request):
    from datetime import datetime
    """Generate pdf."""
    # Model data
    my_obj = Lesson.objects.get(title="Getting Started")
    people = Lesson.objects.all().exclude(id=my_obj.id)
    #barcode = gen_barcode('123456789102')
    #print(settings.STATIC_ROOT)
    # Rendered
    html_string = render_to_string('lessons/pdf.html', {'lessons': people,'object':my_obj,'current_date_and_time':datetime.now(),'Website_address':'http://learn.pythonanywhere.com','user':request.user})
    html = HTML(string=html_string, base_url=request.build_absolute_uri()).write_pdf(stylesheets=[CSS(settings.STATIC_ROOT +  '/css/materialize.css')],presentational_hints=True)
    result = html#.write_pdf()

    # Creating http response
    response = HttpResponse(result,content_type='application/pdf;')
    #response['Content-Disposition'] = 'inline; filename=list_people.pdf'
    response['Content-Disposition'] = 'filename="pywe_tutorial.pdf"'
    #response['Content-Transfer-Encoding'] = 'binary'
    #with tempfile.NamedTemporaryFile(delete=True) as output:
     #   output.write(result)
      #  output.flush()
       # output = open(output.name, 'rb')
        #response.write(output.read())

    return response

import json
def create_lessons(request):

    url = "http://learn.pythonanywhere.com/lessonapi/Lesson/?username=Ellie&api_key=faa66b4640ed7482fc21007016db22174fe6d26dd0a0af33d7761af49a5b&html=true&limit=26"
    resp = r.get(url)
    new = open('lessons.json', 'w+')
    new = new.write(resp.text)


    new = open('lessons.json', 'r+')
    new = new.read()
    resp = json.loads(new)
    objs = resp['objects']
    for lesson in objs:
        try:
            obj = Lesson(title=lesson["title"],body=lesson["body"],intro_text=lesson["intro_text"],user=request.user)
            obj.save()
        except:
            return HttpResponse("Failure")
        else:
            return HttpResponse("Lessons created")

    return HttpResponse("Success")