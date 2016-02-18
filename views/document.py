from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from ..models.document import Document
from ..models.page import Page

class OwnerMixin(object):
	def get_queryset(self):
		qs = super(OwnerMixin, self).get_queryset()
		return qs.filter(owner=self.request.user)

class OwnerEditMixin(object):
	def form_valid(self, form):
		form.instance.owner = self.request.user
		return super(OwnerEditMixin, self).form_valid(form)

class OwnerDocumentMixin(OwnerMixin, LoginRequiredMixin):
	model = Document

class OwnerDocumentEditMixin(OwnerDocumentMixin, OwnerEditMixin):
	fields = ['title', 'file', 'subject']
	success_url = reverse_lazy('manage_document_list')
	template_name = 'document/form.html'

class ManageDocumentListView(OwnerDocumentMixin, ListView):
	template_name = 'document/list.html'

class CreateDocumentView(PermissionRequiredMixin, OwnerDocumentEditMixin, CreateView):
	permission_required = 'CSE371Project.add_document'

class DocumentUpdateView(PermissionRequiredMixin, OwnerDocumentEditMixin, UpdateView):
	permission_required = 'CSE371Project.change_document'

class DocumentDeleteView(PermissionRequiredMixin, OwnerDocumentMixin, DeleteView):
	template_name = 'document/delete.html'
	success_url = reverse_lazy('manage_document_list')
	permission_required = 'CSE371Project.delete_document'

class DocumentDetailView(LoginRequiredMixin, DetailView):
	model = Document
	template_name = 'document/detail.html'
	def pages(self):
		return Page.objects.filter(document = self.kwargs['pk'])
