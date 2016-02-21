from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.views.generic import CreateView, UpdateView, DeleteView ,ListView, DetailView
from django.core.urlresolvers import reverse_lazy
from ..models.subject import Subject
from ..models.document import Document

class CreateSubject(PermissionRequiredMixin, LoginRequiredMixin, CreateView):
    model = Subject
    fields = ('title',)
    template_name = 'subject/form.html'
    permission_required = 'CSE371Project.add_subject'
    raise_exception = True

class DeleteSubject(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Subject
    success_url = reverse_lazy('list_subject')
    template_name = 'subject/confirm_delete.html'
    permission_required = 'CSE371Project.delete_subject'

class DetailSubject(LoginRequiredMixin, DetailView):
    model = Subject
    template_name = 'subject/detail.html'
    def documents(self):
        return Document.objects.filter(subject_id = self.kwargs['pk'])

class ListSubject(LoginRequiredMixin, ListView):
    model = Subject
    template_name = 'subject/list.html'

class UpdateSubject(PermissionRequiredMixin, UpdateView):
    model = Subject
    fields = ('title',)
    template_name = 'subject/form.html'
    permission_required = 'CSE371Project.change_subject'
