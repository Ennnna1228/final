from django.urls import path
from .views import *
from . import views

urlpatterns = [
path("", UpdateoptionList.as_view(), name = 'updateoption_list'),
path("<int:pk>/", UpdateoptionView.as_view(), name = 'updateoption_view'),
path("register/", views.register_view, name='register'),
path("<int:pk>/create/", WorkCreate.as_view(),name = 'work_create'),
path("class/",ClassesList.as_view(),name = 'class_list'),
path('audit/list/', TeacherAuditListView.as_view(), name='teacher_audit_list'),
path('audit/<int:pk>/', TeacherAuditUpdateView.as_view(), name='teacher_audit_work'),
]