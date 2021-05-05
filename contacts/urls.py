from django.urls import path
from .views import *

app_name = 'friends'

urlpatterns = [
    path('', index, name='homepage'),
    path('update/<int:id>', update, name='update'),
    path('delete/<int:id>', delete, name='delete'),
    path('download/', download, name='backup')
]
