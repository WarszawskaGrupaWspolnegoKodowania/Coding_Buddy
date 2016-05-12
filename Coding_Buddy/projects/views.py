from django.shortcuts import render
from django.views.generic import DetailView, ListView, RedirectView, UpdateView
from .models import Project

class ProjectListView(ListView):
    model = Project
    # These next two lines tell the view to index lookups by username
    slug_field = "name"
    slug_url_kwarg = "name"
