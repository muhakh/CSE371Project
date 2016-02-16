from django.conf.urls import url
from django.contrib import admin
from .views.subject import CreateSubject , UpdateSubject, DeleteSubject, ListSubject
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^subject/create/$', CreateSubject.as_view(), name='create_subject'),
    url(r'^subject/update/(?P<slug>[a-z0-9-]+)$', UpdateSubject.as_view(), name='update_subject'),
    url(r'^subject/delete/(?P<slug>[a-z0-9-]+)$', DeleteSubject.as_view(), name='delete_subject'),
    url(r'^subject/view/(?P<slug>[a-z0-9-]+)$', ListSubject.as_view(), name='view_subject')
]
