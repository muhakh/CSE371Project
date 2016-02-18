from django.db import models
from django.template.defaultfilters import slugify

class Subject(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    def __str__(self):
        return self.title
    class Meta:
        ordering = ('title',)
    def save(self):
        super(Subject, self).save()
    	self.slug = slugify(self.title)
    	super(Subject, self).save()
    def get_absolute_url(self):
        return "/subject/view/%s/" % self.slug
