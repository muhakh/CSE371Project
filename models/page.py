from __future__ import unicode_literals
from django.db import models
from .document import Document
from django.dispatch import receiver
from django.db.models.signals import post_save
from ..pdf2png import convert

class Page(models.Model):
    image = models.ImageField(upload_to='documents/%Y/%m/%d')
    document = models.ForeignKey(Document)
    likes_count = models.PositiveIntegerField()
    def __str__(self):
        return str(self.document) + " | Page no. " + str(self.id)
    def url_as_list(self):
        return self.image.split('.')
@receiver(post_save, sender=Document)
def document_post_save(sender, **kwargs):
		page_i = convert(kwargs['instance'].file.path)
		for i in range (page_i):
			p = Page.objects.create(document_id = kwargs['instance'].id, image = kwargs['instance'].file.name+str(i)+'.png', likes_count = 0)
			p.save()
