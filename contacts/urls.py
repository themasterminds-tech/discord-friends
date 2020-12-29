from django.urls import path
from .views import index, delete, update, view

app_name = 'friends'

urlpatterns = [
    path('', index, name='homepage'),
    path('friend/<int:id>', view, name='view'),
    path('update/<int:id>', update, name='update'),
    path('delete/<int:id>', delete, name='delete')
]
