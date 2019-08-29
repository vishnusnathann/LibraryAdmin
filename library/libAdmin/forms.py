from django import forms
from django.forms import widgets
class LoginForm(forms.Form):
	username = forms.CharField(widget=forms.TextInput())
	password = forms.CharField(widget=forms.PasswordInput())

class BookForm(forms.Form):
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.fields['avail'].initial = 'True'
		self.fields['avail'].required = False

	book_name = forms.CharField(label='Book Name')  
	author = forms.CharField(label='Author')
	price = forms.CharField(label='price')
	avail=forms.BooleanField(label='Available')

    