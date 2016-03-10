from django.db import models
from django.contrib.auth.models import User
from .document import Document
from .page import Page

class Comment(models.Model):
    content = models.TextField()
    owner = models.ForeignKey(User)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    class Meta:
        abstract = True
    def __str__(self):
        return self.content

class DocumentComment(Comment):
    document = models.ForeignKey(Document, related_name='dcomment')

class PageComment(Comment):
    page = models.ForeignKey(Page, related_name='pcomment')
