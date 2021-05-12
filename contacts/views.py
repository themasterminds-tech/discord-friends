from django.http.response import HttpResponse
from django.shortcuts import render
from .models import Friends
from .forms import FriendForm, RegisterForm, UploadForm
from django.http import HttpResponseRedirect
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .databases import extract_postgresql
import csv
from django.conf import settings
import os


# INDEX view
def index(request):

    # Create register form
    register_form = RegisterForm()

    # Variables to pass to the template
    context = {
        'form_register': register_form,
    }

    if request.user.is_authenticated:
        form = FriendForm(request.POST or None)
        upload_form = UploadForm()

        contacts = Friends.objects.filter(
            account=request.user).order_by('username')
        has_friends = bool(contacts)

        paginator = Paginator(contacts, 6)
        page = request.GET.get('page', 1)

        try:
            contacts = paginator.page(page)
        except PageNotAnInteger:
            contacts = paginator.page(1)
        except EmptyPage:
            contacts = paginator.page(paginator.num_pages)

        context['contacts'] = contacts
        context['form'] = form
        context['has_friends'] = has_friends
        context['upload_form'] = upload_form

        if request.method == "POST":

            user_id = request.POST.get('user_id')
            username = request.POST.get('username')
            tag = request.POST.get('tag')

            contact = Friends.objects.create(
                user_id=user_id, username=username, tag=tag, account=request.user)

            contact.save()

            messages.success(request, 'Successfully created discord profile!')
            return HttpResponseRedirect('/')

    return render(request, 'contacts/index.html', context)


# DELETE view
@login_required(login_url='/')
def delete(request, id):
    if request.method == "POST":
        friend = Friends.objects.get(id=id)
        friend.delete()
        return HttpResponseRedirect('/')
    elif request.method == "GET":
        messages.error(request, "That url doesn't support GET requests")
        return HttpResponseRedirect('/')


# UPDATE view
@login_required(login_url='/')
def update(request, id):

    friend = Friends.objects.get(id=id)

    if request.user.is_authenticated:
        if request.method == "POST":
            username = request.POST.get('username')
            tag = request.POST.get('tag')

            friend.username = username
            friend.tag = tag

            friend.save()

            messages.success(request, 'Successfully updated discord profile!')
            return HttpResponseRedirect('/')

        elif request.method == "GET":
            messages.error(request, "That url doesn't support GET requests!")
            return HttpResponseRedirect('/')


# DOWNLOAD view
@login_required(login_url='/')
def download(request):
    extract_postgresql()
    return render(request, 'contacts/download.html', context={})


# UPLOAD view
@login_required(login_url='/')
def upload(request):
    if request.method == "POST":

        upload_form = UploadForm(request.POST or None, request.FILES or None)

        if upload_form.is_valid():

            # File gotten from request
            file = request.FILES.get('upload')

            # Decoded file content
            blob = file.read().decode()

            tmp_file_exists = os.path.exists(
                f'{settings.BASE_DIR}/temp/uploadedfilecache.tmp')

            # Check if the temporary file exists
            if not tmp_file_exists:
                open(f'{settings.BASE_DIR}/temp/uploadedfilecache.tmp', mode='x')

            # Write data to the file
            with open(f'{settings.BASE_DIR}/temp/uploadedfilecache.tmp', mode='w', encoding='utf-8') as csv_file:
                csv_file.write(blob)

            # Read the file and create data based on the values
            with open(f'{settings.BASE_DIR}/temp/uploadedfilecache.tmp', mode='r', encoding='utf-8') as csv_file:
                reader = csv.DictReader(
                    csv_file, delimiter=',', dialect='excel')

                for row in reader:
                    username = row.get('username')
                    user_id = row.get('user_id')
                    tag = row.get('tag')

                    if username is not None and user_id is not None and tag is not None:
                        Friends.objects.filter(account=request.user).get_or_create(
                            username=username, user_id=user_id, tag=tag, account_id=request.user.id)
                        messages.success(
                            request, 'Successfully import data from file!')
                        return HttpResponseRedirect('/')
                    else:
                        messages.error(
                            request, "Sorry the file you uploaded isn't a legit csv file or is corrupted!")
                        return HttpResponseRedirect('/')

        else:
            messages.error(
                request, "Sorry I don't support reading of other files apart from csv and txt files!")
            return HttpResponseRedirect('/')

    elif request.method == "GET":
        messages.error(request, "That url doesn't support GET requests!")
        return HttpResponseRedirect('/')
