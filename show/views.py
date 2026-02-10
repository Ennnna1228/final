from django.shortcuts import render
from django.views.generic import ListView,CreateView,DetailView
from .models import *
from django.urls import reverse_lazy


# Create your views here.
class WorkList(ListView):
    model = works

class UpdateoptionList(ListView):
    model = updateoption

class ClassesList(ListView):
    model = classes

class WorkCreate(CreateView):
    model = works
    fields = '__all__'
    success_url = reverse_lazy('work_list')

class UpdateoptionView(DetailView):
    model = updateoption

    def get_context_data(self, **kwargs):

        ctx = super().get_context_data(**kwargs)
        ctx['work_list'] = works.objects.filter(topic_id = self.object.id)
        return ctx 