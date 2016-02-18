from django.conf.urls import url
from .views import document
from .views.subject import CreateSubject , UpdateSubject, DeleteSubject, DetailSubject, ListSubject
from .views.page import PageList , PageDetail

urlpatterns = [
	url(r'^document/(?P<pk>\d+)/$', document.DocumentDetailView.as_view(), name='document_detail'),
	url(r'^document/create/$', document.CreateDocumentView.as_view(), name='document_create'),
	url(r'^document/(?P<pk>\d+)/edit/$', document.DocumentUpdateView.as_view(), name='document_edit'),
	url(r'^document/(?P<pk>\d+)/delete/$', document.DocumentDeleteView.as_view(), name='document_delete'),
	url(r'^$', ListSubject.as_view(), name='list_subject'),
	url(r'^subject/create/$', CreateSubject.as_view(), name='create_subject'),
    url(r'^subject/update/(?P<slug>[a-z0-9-]+)$', UpdateSubject.as_view(), name='update_subject'),
    url(r'^subject/delete/(?P<slug>[a-z0-9-]+)$', DeleteSubject.as_view(), name='delete_subject'),
    url(r'^subject/view/(?P<pk>\d+)/$', DetailSubject.as_view(), name='view_subject'),
	url(r'^page/(?P<pk>\d+)/$', PageDetail.as_view(), name='page_detail'),
]
