from django.urls import path
from app1.views import *
app_name='aaa'
urlpatterns=[
    path('hai/',hai,name='hai')
]