from django.conf.urls import url
from . import views
urlpatterns = [
	url(r'^mine/$',	views.ManageDocumentListView.as_view(), name='manage_document_list'),
	url(r'^create/$', views.CreateDocumentView.as_view(),	name='document_create'),
	url(r'^(?P<pk>\d+)/edit/$',	views.DocumentUpdateView.as_view(), name='document_edit'),
	url(r'^(?P<pk>\d+)/delete/$', views.DocumentDeleteView.as_view(), name='document_delete'),
]

