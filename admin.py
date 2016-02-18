from django.contrib import admin

from .models.subject import Subject
from .models.document import Document
from .models.page import Page
from .models.comment import  DocumentComment , PageComment

admin.site.register(Subject)
admin.site.register(Document)
admin.site.register(Page)
admin.site.register(DocumentComment)
admin.site.register(PageComment)
