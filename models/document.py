from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Document(models.Model):
	owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='courses_created')
	subject = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name='courses')
	title = models.CharField(max_length=200)
	slug = models.SlugField(max_length=200, unique=True)
	file = models.FileField(upload_to='')
	created = models.DateTimeField(auto_now_add=True)
	class Meta:
		ordering = ('-created',)
	def __str__(self):
		return self.title