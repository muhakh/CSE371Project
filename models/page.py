from __future__ import unicode_literals
from django.db import models
class Page(models.Model):
    image=models.ImageField(upload_to='documents/%Y/%m/%d')
    #document=models.ForeignKey()
    likes_count=models.PositiveIntegerField()
