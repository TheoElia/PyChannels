from tastypie.resources import ModelResource
from .models import Lesson
from tastypie.authorization import Authorization
# from tastypie.authorization import DjangoAuthorization
from tastypie.authentication import ApiKeyAuthentication
from tastypie.serializers import Serializer
from django.utils.html import strip_tags

# class that makes user gets only Sms objects they created.
class LessonAuthorization(Authorization):
    # Method to fetch all objects created by the user
    def read_list(self, object_list, bundle):
        return object_list.all()
    # Method to filter only lesson objects created by the user
    #def read_detail(self, object_list, bundle):
     #   obj = object_list[0]
      #  return obj.user == bundle.request.user



class LessonResource(ModelResource):
    class Meta:
        queryset = Lesson.objects.all()
        resource_name = 'Lesson'
        fields = ['title', 'intro_text','body','date_created']
        authorization = LessonAuthorization()
        authentication = ApiKeyAuthentication()
        always_return_data = True
        serializer = Serializer()


    # Method to add user who created an sms object without browsers
    def hydrate(self, bundle):
        bundle.obj.user = bundle.request.user
        return bundle
    # Method to add the sms_id from object id
    def dehydrate(self, bundle):
        bundle.data['lesson_id'] = bundle.obj.id
        bundle.data['created_by'] = bundle.obj.user
        try:
            html = bundle.request.GET.get('html')
        except:
            pass
        else:
            if html not in ('true','True'):
                bundle.data['body'] = strip_tags(bundle.obj.body)
        #bundle.data['body'] = strip_tags(bundle.obj.body)
        return bundle
    # Determine format returned
    def determine_format(self, request):
        if request.GET.get('format')=='xml':
            return 'application/xml'

        if request.GET.get('format')=='json':
            return 'application/json'

        if request.GET.get('format')=='jsonp':
            return 'text/javascript'

        if request.GET.get('format')=='yaml':
            return 'text/yaml'

        if request.GET.get('format')=='plist':
            return 'text/plist'

        if request.GET.get('format')=='html':
            return 'text/html'


        if not request.GET.get('format'):
            return 'application/json'



    def text_type(self, request):
        if request.GET.get('html') in ('true','True'):
            return True
        else:
            return False

	# authorization = Authorization()

