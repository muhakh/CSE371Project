from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.views.generic import CreateView, UpdateView, DeleteView ,ListView, DetailView
from django.shortcuts import get_object_or_404
from ..models.subject import Subject
from ..models.document import Document

class CreateSubject(CreateView):
    model = Subject
    fields = ('title',)
    template_name = 'subject/form.html'

class DeleteSubject(DeleteView):
    model = Subject

class DetailSubject(LoginRequiredMixin, DetailView):
    model = Subject
    template_name = 'subject/detail.html'
    def documents(self):
        return Document.objects.filter(subject_id = self.kwargs['pk'])

class ListSubject(LoginRequiredMixin, ListView):
    model = Subject
    template_name = 'subject/list.html'

class UpdateSubject(UpdateView):
    model = Subject
    fields = ('title',)
    template_name = 'subject/form.html'
