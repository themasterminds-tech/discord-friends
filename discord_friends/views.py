from django.http.response import HttpResponseRedirect
from django.contrib.auth import logout


def _logout(request):
    logout(request)
    return HttpResponseRedirect('/')
