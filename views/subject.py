from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import CreateView, UpdateView, DeleteView ,ListView
from ..models.subject import Subject

class CreateSubject(CreateView):
    model = Subject


class DeleteSubject(DeleteView):
    model = Subject

class ListSubject(ListView):
    model = Subject

class UpdateSubject(UpdateView):
    model = Subject

