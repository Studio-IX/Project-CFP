from django.urls import path
from .views import *
urlpatterns = [
    path('', register01 , name="register01"),
    path('register02/', register02 , name="register02"),
    path('register03/', register03 , name="register03"),
    path('register04/', register04 , name="register04"),
    path('register05/', register05 , name="register05"),
    path('login/', login, name="login"),
]
