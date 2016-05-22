from django.shortcuts import render
from django.views.generic import DetailView, ListView, UpdateView, CreateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from .models import Project
from .forms import ProjectForm

class ProjectListView(ListView):
    model = Project

class ProjectDetailView(DetailView):
    model = Project

class ProjectCreateView(CreateView):
    model = Project
    form_class = ProjectForm
    def get_success_url(self):
        return reverse_lazy('projects:detail', args=(self.object.slug,)) 

class ProjectUpdateView(UpdateView):
    model = Project
    form_class = ProjectForm
    def get_success_url(self):
        return reverse_lazy('projects:detail', args=(self.object.slug,)) 

class ProjectDeleteView(DeleteView):
    model = Project
    success_url = reverse_lazy('projects:list')
