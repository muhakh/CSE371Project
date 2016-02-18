from django.conf.urls import url
from . import views
urlpatterns = [
	url(r'^mine/$',	views.document.ManageDocumentListView.as_view(), name='manage_document_list'),
	url(r'^create/$', views.document.CreateDocumentView.as_view(),	name='document_create'),
	url(r'^(?P<pk>\d+)/edit/$',	views.document.DocumentUpdateView.as_view(), name='document_edit'),
	url(r'^(?P<pk>\d+)/delete/$', views.document.DocumentDeleteView.as_view(), name='document_delete'),
]
