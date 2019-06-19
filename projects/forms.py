from django import forms

class SignInForm(forms.Form):
	username = forms.CharField(label='Username', max_length=100, widget=forms.TextInput(
			attrs={
				'class': 'form-control',
				'placeholder': 'Username',
				'autocomplete': 'off'
			}
		))
	password = forms.CharField(label='Password', max_length=100, widget=forms.TextInput(
			attrs={
				'class': 'form-control',
				'placeholder': 'Password',
				'type':'password'
			}
		))

class CreateAccountForm(forms.Form):
	firstname = forms.CharField(label='First name', max_length=100, widget=forms.TextInput(
			attrs={
				'class': 'form-control',
				'placeholder': 'First name',
				'autocomplete': 'off'
			}
		))
	lastname = forms.CharField(label='Last name', max_length=100, widget=forms.TextInput(
			attrs={
				'class': 'form-control',
				'placeholder': 'Last name',
				'autocomplete': 'off'
			}
		))
	username = forms.CharField(label='Username', max_length=100, widget=forms.TextInput(
			attrs={
				'class': 'form-control',
				'placeholder': 'Username',
				'autocomplete': 'off'
			}
		))
	password = forms.CharField(label='Password', max_length=100, widget=forms.TextInput(
			attrs={
				'class': 'form-control',
				'placeholder': 'Password',
				'type':'password'
			}
		))

class CreateProjectForm(forms.Form):
	name = forms.CharField(label='Name', max_length=100, widget=forms.TextInput(
		attrs={
			'class': 'form-control',
			'placeholder': 'Name',
			'autocomplete': 'off'
		}
	))

class CreateTaskForm(forms.Form):
	name = forms.CharField(label='Name', max_length=100, widget=forms.TextInput(
		attrs={
			'class': 'form-control',
			'placeholder': 'Name',
			'autocomplete': 'off'
		}
	))

