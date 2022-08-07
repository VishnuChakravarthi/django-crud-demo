from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView

from . import models

# Create your views here.


class IndexPage(TemplateView):
    template_name = 'index.html'


class SchoolListView(ListView):
    context_object_name = "schools"
    model = models.School


class SchoolDetailView(DetailView):
    context_object_name = "school"
    model = models.School
    template_name = 'class_template_app/school_details.html'


class SchoolCreateView(CreateView):
    fields = "__all__"
    model = models.School
    template_name = 'class_template_app/school_create.html'


class SchoolUpdateView(UpdateView):
    fields = "__all__"
    model = models.School
    template_name = 'class_template_app/school_create.html'


class SchoolDeleteView(DeleteView):
    model = models.School
    success_url = reverse_lazy("app:list")
