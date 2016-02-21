from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models
from .subject import Subject
from django.template.defaultfilters import slugify

class Document(models.Model):
	owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='doucument_owner')
	subject = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name='doucument_subject')
	title = models.CharField(max_length=200)
	slug = models.SlugField(max_length=200, unique=True)
	file = models.FileField(upload_to='')
	created = models.DateTimeField(auto_now_add=True)
	class Meta:
		ordering = ('-created',)
	def save(self):

		self.slug = slugify(self.title)
		super(Document, self).save()

	def __str__(self):
		return self.title
