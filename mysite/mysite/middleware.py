from django.utils.timezone import now
from accounts.models import CustomUser
try:
    from django.utils.deprecation import MiddlewareMixin
except ImportError:
    MiddlewareMixin = object


class SetLastVisitMiddleware:

    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.

    def __call__(self, request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.
        if request.user.is_authenticated:
            #Update last visit time after request finished processing.
            CustomUser.objects.filter(pk=request.user.pk).update(last_activity=now())


        response = self.get_response(request)

        # Code to be executed for each request/response after
        # the view is called.

        return response
    #def __init__(self, next_layer=None):
     #   """We allow next_layer to be None because old-style middlewares
      ## """
        #self.get_response = next_layer

    #def process_response(self, request, response):

     #   return response

    #def __init__(self, get_response=None):
        #self.get_response = get_response
        # One-time configuration and initialization.
        #super(SetLastVisitMiddleware, self).__init__()

    #def __call__(self, request):
     #   if request.user.is_authenticated():
            #Update last visit time after request finished processing.
      #      CustomUser.objects.filter(pk=request.user.pk).update(last_visit=now())
        # Code to be executed for each request before
        # the view (and later middleware) are called.

       # response = self.get_response(request)

        # Code to be executed for each request/response after
        # the view is called.

        #return response