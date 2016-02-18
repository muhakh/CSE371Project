from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^page/comments/$', views.PageCommentListView.as_view(), name='page_comments_list'),
    url(r'^page/comments/(?P<pk>\d+)', views.PageCommentDetailView.as_view(), name='page_comment_detail'),
    url(r'^page/comments/new/$', views.PageCommentCreateView.as_view(), name='page_comment_new'),
    url(r'^document/comments/$', views.DocumentCommentListView.as_view(), name='doc_comments_list'),
    url(r'^document/comments/(?P<pk>\d+)', views.DocumentCommentDetailView.as_view(), name='doc_comment_detail'),
    url(r'^document/comments/new/$', views.DocumentCommentCreateView.as_view(), name='doc_comment_new'),
]
