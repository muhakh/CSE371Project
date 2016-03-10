from ..models.comment import PageComment, DocumentComment
from ..models.page import Page
from ..models.document import Document
from django.views.generic.edit import CreateView
from ..forms import PageCommentForm, DocumentCommentForm
from django.core.urlresolvers import reverse_lazy

class PageCommentCreate(CreateView):
    model = PageComment
    form_class = PageCommentForm
    def get_success_url(self, **kwargs):
		return reverse_lazy('project:page_detail', kwargs={'pk': self.object.page.id})

    def form_valid(self, form):
        form.instance.owner = self.request.user
        form.instance.page = Page.objects.get(id = self.kwargs['pk'])
        return super(PageCommentCreate, self).form_valid(form)

class DocumentCommentCreate(CreateView):
    model = DocumentComment
    form_class = DocumentCommentForm
    def get_success_url(self, **kwargs):
		return reverse_lazy('project:document_detail', kwargs={'pk': self.object.document.id})

    def form_valid(self, form):
        form.instance.owner = self.request.user
        form.instance.document = Document.objects.get(id = self.kwargs['pk'])
        return super(DocumentCommentCreate, self).form_valid(form)
