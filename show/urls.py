from django.urls import path
from .views import *

urlpatterns = [
path("", UpdateoptionList.as_view(), name = 'updateoption_list'),
]