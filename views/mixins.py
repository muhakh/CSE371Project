from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.core.urlresolvers import reverse, reverse_lazy
from ..models.document import Document

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
	def get_success_url(self, **kwargs):
		return reverse_lazy('project:document_detail', kwargs={'pk': self.object.id})
	template_name = 'document/form.html'
