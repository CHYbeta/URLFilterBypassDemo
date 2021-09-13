from django.http import HttpResponseRedirect
from django.urls import reverse
from . import views

class CheckLoginHandler(object):
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        print("request.get_full_path: %s" % request.get_full_path())
        print("request.get_full_path_info: %s" % request.get_full_path_info())
        print("request.path: %s" % request.path)
        print("request.path_info: %s" % request.path_info)
        print("request.get_raw_uri: %s" % request.get_raw_uri())
        print("request.build_absolute_uri: %s" % request.build_absolute_uri())

        if request.user.is_anonymous and not request.get_full_path().endswith("login"):
            return HttpResponseRedirect(reverse(views.login))

        response = self.get_response(request)
        return response

