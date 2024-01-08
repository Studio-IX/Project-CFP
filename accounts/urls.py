from django.urls import path
from .views import *
urlpatterns = [
    path('', register01 , name="register01"),
    path('register/page2', register02 , name="register02"),
    path('register/page3', register03 , name="register03"),
    path('register/page4', register04 , name="register04"),
    path('register/page5', register05 , name="register05"),
    path('login/', login, name="login"),
]
