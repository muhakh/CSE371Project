from django.conf.urls import url
from .views import document
from .views.subject import CreateSubject , UpdateSubject, DeleteSubject, DetailSubject, ListSubject
from .views.page import PageDetail
from .views.comment import PageCommentCreate, DocumentCommentCreate
from .views.register import register
from django.contrib.auth import views as auth_views

urlpatterns = [
	url(r'^accounts/profile/$',	document.ManageDocumentListView.as_view(), name='manage_document_list'),
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
	url(r'^page/(?P<pk>\d+)/comment/new/$', PageCommentCreate.as_view(), name='create_page_comment'),
	url(r'^document/(?P<pk>\d+)/comment/new/$', DocumentCommentCreate.as_view(), name='create_document_comment'),
	url(r'^accounts/register/$', register, name='register'),
]
