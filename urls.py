from django.conf.urls import url
from .views import document
from .views.subject import CreateSubject , UpdateSubject, DeleteSubject, ListSubject

from .views.page import PageList , PageDetail
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
	url(r'^mine/$',	document.ManageDocumentListView.as_view(), name='manage_document_list'),
	url(r'^create/$', document.CreateDocumentView.as_view(),	name='document_create'),
	url(r'^(?P<pk>\d+)/edit/$',	document.DocumentUpdateView.as_view(), name='document_edit'),
	url(r'^(?P<pk>\d+)/delete/$', document.DocumentDeleteView.as_view(), name='document_delete'),
    url(r'^subject/create/$', CreateSubject.as_view(), name='create_subject'),
    url(r'^subject/update/(?P<slug>[a-z0-9-]+)$', UpdateSubject.as_view(), name='update_subject'),
    url(r'^subject/delete/(?P<slug>[a-z0-9-]+)$', DeleteSubject.as_view(), name='delete_subject'),
    url(r'^subject/view/(?P<slug>[a-z0-9-]+)$', ListSubject.as_view(), name='view_subject'),

	url(r'^all/$',PageList.as_view()),
	url(r'^(?P<pk>\d+)/$',PageDetail.as_view()),
	 url(r'^upload/$',views.upload),
]
