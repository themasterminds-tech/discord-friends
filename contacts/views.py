from django.http.response import HttpResponse
from django.shortcuts import render
from .models import Friends
from .forms import FriendForm
from django.http import HttpResponseRedirect
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from rest_framework.decorators import api_view
from .databases import extract_postgresql


# INDEX view
def index(request):
    friends = Friends.objects.all()

    paginator = Paginator(friends, 6)
    page = request.GET.get('page', 1)

    try:
        friends = paginator.page(page)
    except PageNotAnInteger:
        friends = paginator.page(1)
    except EmptyPage:
        friends = paginator.page(paginator.num_pages)

    form = FriendForm(request.POST or None)

    if request.user.is_authenticated:
        if request.method == "POST":
            if form.is_valid():
                form.save()
                return HttpResponseRedirect('/')
            else:
                messages.error(request, 'Invalid information provided')
                return HttpResponseRedirect('/')

    has_friends = bool(friends)

    context = {
        'contacts': friends,
        'has_friends': has_friends,
        'form': form,
    }
    return render(request, 'contacts/index.html', context)


# DELETE view
@login_required
@api_view(['DELETE'])
def delete(request, id):
    friend = Friends.objects.get(id=id)

    friend.delete()

    return HttpResponseRedirect('/')


# UPDATE view
@login_required
def update(request, id):
    friend = Friends.objects.get(id=id)
    form = FriendForm(request.POST or None, instance=friend)

    if request.user.is_authenticated:
        if request.method == "POST":
            if form.is_valid():
                form.save()
                return HttpResponseRedirect('/')
            else:
                messages.error(request, 'Unable to update discord profile')
                return HttpResponseRedirect('/')

    context = {
        'form': form,
        'friend': friend
    }
    return render(request, 'contacts/update.html', context)


@login_required
def backup(request):
    extract_postgresql()
    return render(request, 'contacts/backup.html', context={})
