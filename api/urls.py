from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^page/(?P<pk>\d+)/comments/$', views.PageCommentListView.as_view(), name='page_comments_list'),
    
    url(r'^document/comments/$', views.DocumentCommentListView.as_view(), name='doc_comments_list'),
    url(r'^document/(?P<pk>\d+)/comments/', views.DocumentCommentDetailView.as_view(), name='doc_comment_detail'),
    url(r'^document/comments/new/$', views.DocumentCommentCreateView.as_view(), name='doc_comment_new'),
]
