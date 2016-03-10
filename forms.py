from django import forms
from django.contrib.auth.models import User
from models.document import Document
from models.comment import PageComment, DocumentComment

class DocumentUploadForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ['title', 'subject', 'file']

class PageCommentForm(forms.ModelForm):
    class Meta:
        model = PageComment
        fields = ['content',]

class DocumentCommentForm(forms.ModelForm):
    class Meta:
        model = DocumentComment
        fields = ['content',]
class UserRegistrationForm(forms.ModelForm):
	password = forms.CharField(label='Password', widget=forms.PasswordInput)
	password2 = forms.CharField(label='Repeat password', widget=forms.PasswordInput)
	class Meta:
		model = User
		fields = ('username', 'first_name','last_name', 'email')

	def clean_password2(self):
		cd = self.cleaned_data
		if cd['password'] != cd['password2']:
			raise forms.ValidationError('Passwords don\'t match. Please, re-enter the password')
			return cd['password2']
