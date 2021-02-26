""" Routes """

from django.contrib import admin
from django.urls import path, include
from .views import _logout


urlpatterns = [
    path('admin/', admin.site.urls),
    path('logout/', _logout, name='logout'),
    path('', include('contacts.urls')),
    path('', include('pwa.urls')),
]
