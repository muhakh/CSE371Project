from django.db import models


class Subject(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField()
    def __str__(self):
        return self.title
    class Meta:
        pass

