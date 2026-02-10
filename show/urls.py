from django.urls import path
from .views import *

urlpatterns = [
path("", UpdateoptionList.as_view(), name = 'updateoption_list'),
path("<int:pk>/", UpdateoptionView.as_view(), name = 'updateoption_view'),
path("update/",WorkCreate.as_view(), name = 'work_create'),
]