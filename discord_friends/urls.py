# Project routing

from django.contrib import admin
from django.urls import path, include
from .views import _logout, _login, _register

urlpatterns = [
    path('backend/admin/', admin.site.urls),
    path('logout/', _logout, name='logout'),
    path('register/', _register, name='register'),
    path('login/', _login, name='login'),
    path('', include('contacts.urls'), name='homepage'),
    path('', include('pwa.urls')),
]
