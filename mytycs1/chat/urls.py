# chat/urls.py

from django.urls import path
from .views import message_api

urlpatterns = [
    path('api/message/', message_api, name='message_api'),
]
