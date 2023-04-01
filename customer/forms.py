from allauth.account.forms import SignupForm
from django import forms


class CustomSignupForm(SignupForm):
	first_name = forms.CharField(max_length=30, label='First name')
	last_name = forms.CharField(max_length=30, label='Last name')
	phone = forms.CharField(max_length=30, label='Phone number')
	def save(self, request):
		user = super(CustomSignupForm, self).save(request)
		user.first_name = self.cleaned_data['first_name']
		user.last_name = self.cleaned_data['last_name']
		user.phone = self.cleaned_data['phone']
		user.save()
		return user

