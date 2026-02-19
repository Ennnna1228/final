from django.shortcuts import render, redirect
from django.views.generic import ListView,CreateView,DetailView
from .models import *
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login


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
    works.topic_id = ['pk']

class UpdateoptionView(DetailView):
    model = updateoption

    def get_context_data(self, **kwargs):

        ctx = super().get_context_data(**kwargs)
        ctx['work_list'] = works.objects.filter(topic_id = self.object.id)
        return ctx 

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = UserCreationForm.Meta.fields + ('role',)

def register_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('updateoption_list')
    else:
        form = CustomUserCreationForm()
        
    return render(request, 'register.html', {'form': form})