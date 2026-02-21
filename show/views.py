from django.shortcuts import render, redirect,get_object_or_404
from django.views.generic import ListView,CreateView,DetailView,UpdateView
from .models import *
from .urls import *
from django.urls import reverse_lazy,reverse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.mixins import UserPassesTestMixin

# Create your views here.
class UpdateoptionList(ListView):
    model = updateoption

class ClassesList(ListView):
    model = classes

class WorkCreate(CreateView):
    model = works
    fields = ['title', 'desc', 'jpg', 'classes_id', 'Certification']

    def get_success_url(self):
        return reverse('updateoption_list')
    
    def form_valid(self, form):
        pk_from_url = self.kwargs.get('pk')
        form.instance.topic_id = pk_from_url
        option = get_object_or_404(updateoption, id=pk_from_url)
        option.amount += 1
        option.save()
        return super().form_valid(form)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pk_from_url = self.kwargs.get('pk')
        target_option = get_object_or_404(updateoption, id=pk_from_url)
        context['target_option'] = target_option
        context['all_classes'] = classes.objects.all()
        return context
    
class UpdateoptionView(DetailView):
    model = updateoption

    def get_context_data(self, **kwargs):

        ctx = super().get_context_data(**kwargs)
        ctx['updateoption_list'] = works.objects.filter(topic_id = self.object.id)
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

class TeacherAuditListView(UserPassesTestMixin, ListView):
    model = works
    template_name = 'show/teacher_audit_list.html'
    context_object_name = 'audit_works'

    def test_func(self):
        return self.request.user.is_staff

    def get_queryset(self):
        return works.objects.filter(Certification=True, audit_status='pending')

class TeacherAuditUpdateView(UserPassesTestMixin, UpdateView):
    model = works
    fields = ['audit_status', 'teacher_comment'] # 老師只能改這兩個欄位
    template_name = 'show/teacher_audit_form.html'
    success_url = reverse_lazy('teacher_audit_list')

    def test_func(self):
        return self.request.user.is_staff