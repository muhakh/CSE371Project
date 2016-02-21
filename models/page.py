from __future__ import unicode_literals
from django.db import models
from .document import Document

class Page(models.Model):
    image = models.ImageField(upload_to='documents/%Y/%m/%d')
    document = models.ForeignKey(Document)
    likes_count = models.PositiveIntegerField()
    def __str__(self):
        return str(self.image)
