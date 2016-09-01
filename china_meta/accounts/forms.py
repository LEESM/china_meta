from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignupForm(UserCreationForm):
	username = forms.EmailField(
		required=True,
		widget=forms.EmailInput(
				attrs={
					'class':'hidden',
					'id':'signup_form_username',
					'placeholder':'아이디',
					'required':'True',
				}
			)
		)
	email = forms.EmailField(
		required=True,
		widget=forms.EmailInput(
				attrs={
					'class':'form-control',
					'id':'signup_form_email',
					'placeholder':'邮箱',
					'required':'True',
				}
			)
		)

	password1 = forms.CharField(
		label = ("密码"),
		widget = forms.PasswordInput,
		)

	password2 = forms.CharField(
		label = ("密码"),
		widget = forms.PasswordInput,
		)


	class Meta:
		model=User
		fields = ("email","password1","password2",)

