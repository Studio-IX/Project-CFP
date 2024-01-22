from django.urls import path
from .views import *
urlpatterns = [
    path('', home, name="homepage"),
    path('dashboard/', dashboard, name="dashboard")
]
