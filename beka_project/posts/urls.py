from django.urls import path
from .views import *
urlpatterns = [
    path('registration/', createuser, name="create_user"),
    ]