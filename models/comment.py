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
        app_label = "gallery"
    def __str__(self):
        return self.content

class DocumentComment(models.Model):
    document = models.ForeignKey(Document)

class PageComment(models.Model):
    page = models.ForeignKey(Page)
