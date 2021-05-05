from django.http import HttpResponseRedirect
from django.contrib.auth import logout, login, authenticate
from contacts.forms import RegisterForm
from django.contrib import messages


def _logout(request):
    logout(request)
    return HttpResponseRedirect('/')


def _register(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            register_form = RegisterForm(request.POST or None)

            if register_form.is_valid():
                register_form.save()
                messages.success(
                    request, 'You can now continue to logging in to your brand new account')
                return HttpResponseRedirect('/')
            else:
                messages.error(
                    request, 'Sorry you didn\'t meet up to the registration requirements')
                return HttpResponseRedirect('/')


def _login(request):
    if not request.user.is_authenticated:
        if request.method == "POST":

            username = request.POST.get('username')
            pwd = request.POST.get('pwd')
            instance = authenticate(request, username=username, password=pwd)

            if instance is not None:
                login(request, instance)
                return HttpResponseRedirect('/')
            else:
                messages.error(
                    request, 'Login failed, check entered credentials!')
                return HttpResponseRedirect('/')
