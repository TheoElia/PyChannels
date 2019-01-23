from tastypie.resources import ModelResource
from .models import File
from tastypie.authorization import Authorization
from tastypie.authorization import DjangoAuthorization
from tastypie.authentication import ApiKeyAuthentication
from django.shortcuts import render, redirect,HttpResponse,HttpResponseRedirect
import pyrebase
import json
import os


config = {"apiKey": "AIzaSyCvL086JynApAhRlwALt5TnRkuh6ojKIA4",  "authDomain": "pywe-92968.firebaseapp.com",
            "databaseURL": "https://pywe-92968.firebaseio.com",  "storageBucket": "pywe-92968.appspot.com",
            "serviceAccount": "/home/Learn/mysite/static/fireapi/pywe-92968-a64c4a2fa3da.json"}
firebase = pyrebase.initialize_app(config)
#"projectId": "pywe-92968",
#"messagingSenderId": "591931135706"}
#"serviceAccount": "/home/theoelia/PycharmProjects/face_recog/pywe-92968-a64c4a2fa3da.json",}
firebase = pyrebase.initialize_app(config)

storage = firebase.storage()

auth = firebase.auth()

class pywebase:
# authenticate a user
    def get_token(self,email="gregeace@gmail.com",password="hello222"):
        user = auth.sign_in_with_email_and_password(email,password )
        token = user['idToken']
        return token

    def upload_photo(self,firebase_path, file_path, token):
        try:
            storage.child(firebase_path).put(file_path,token)
        except Exception as e:
            content = e
            error = {"code": 401, "status": False, "error":content,"url":None}
            return error
        else:
            url = storage.child(firebase_path).get_url(token)
            success = {"url":url,"status":True,"code":201}
            return success

# class that makes user gets only Sms objects they created.
class FileAuthorization(Authorization):
# Method to fetch all objects created by the user
	def read_list(self, object_list, bundle):
		return object_list.filter(user=bundle.request.user)

# Method to filter only sms objects created by the user
	def read_detail(self, object_list, bundle):
    		obj = object_list[0]
    		return obj.user == bundle.request.user


class FileResource(ModelResource):
    class Meta:
        queryset = File.objects.all()
        resource_name = 'File'
    fields = ['name','download_url','date_created']
    authorization = FileAuthorization()
    authentication = ApiKeyAuthentication()
	#always_return_data = True

    def deserialize(self, request, data, format=None):
        pywebaseobj = pywebase()
        if not format:
            format = request.META.get('CONTENT_TYPE', 'application/json')
        if format =='application/x-www-form-urlencoded':
            return request.POST
        if format.startswith('multipart'):
            data = request.POST.copy()
            photo = File()
            photo.img = request.FILES['img']
            photo.name = request.POST.get('name')
            photo.firebase_path = "users/{}".format(request.POST.get('name'))
            photo.file_path = request.FILES['img']
            photo.user = request.user
            photo.download_url = pywebaseobj.upload_photo(file_path=request.FILES['img'], firebase_path="users/{}".format(request.POST.get('name')),token=pywebaseobj.get_token())['url']
            #photo.pub_date = request.POST.get('pub_date')
            photo.save()
            # ... etc
            return data
        return super(FileResource, self).deserialize(request, data, format)

	# overriding the save method to prevent the object getting saved twice
    def obj_create(self, bundle, request=None, **kwargs):
         return bundle



    #def alter_detail_data_to_serialize(self,request,data):
     #   return data.get('recepient',[])
# Method to add user who created an sms object without browsers
    def hydrate(self, bundle):
	#bundle.obj.download_url = upload_photo(bundle.obj.filepath, bundle.obj.filename)['url']
    	return bundle

    def dehydrate(self, bundle):
    	#bundle.data['file_id'] = bundle.obj.id
        user_file_objs = File.objects.filter(user = bundle.request.user)
	#latest_file_obj = user_file_objs[len(user_file_objs)-1]
	#bundle.data['download_url'] = latest_file_obj.download_url
	#bundle.data['name'] = latest_file_obj.name
	#bundle.data['error'] =  upload_photo(bundle.obj.filepath, bundle.obj.filename)['error']
        #bundle.data['recipients'] = bundle.obj.recepient
        return bundle








