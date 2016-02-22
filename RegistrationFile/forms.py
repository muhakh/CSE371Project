from django.contrib.auth.models import User
from django import forms

#you should install django-registration by typing:
# pip install django-registration
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
