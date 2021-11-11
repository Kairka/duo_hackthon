from django.db.models import Q
from django.shortcuts import redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from .models import Category, Tour


class TourListView(ListView):
    model = Tour
    template_name = 'home.html'
    context_object_name = 'tours'

