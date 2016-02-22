from django import forms
from models.document import Document
from .pdf2png import convert

class DocumentUploadForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ['title', 'subject', 'file']
    
