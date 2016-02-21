from django import forms
from models.document import Document

class DocumentUploadForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ['title', 'subject', 'file']
