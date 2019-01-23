from django.utils.timezone import now
from .models import CustomUser

class SetLastVisitMiddleware(object):
    def __init__(self, next_layer=None):
        """We allow next_layer to be None because old-style middlewares
        won't accept any argument.
        """
        self.get_response = next_layer

    def process_response(self, request, response):
        if request.user.is_authenticated():
            # Update last visit time after request finished processing.
            CustomUser.objects.filter(pk=request.user.pk).update(last_visit=now())
        return response