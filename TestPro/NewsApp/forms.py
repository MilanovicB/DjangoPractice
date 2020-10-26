from django import forms


class RegistrationForm(forms.Form):
    username = forms.CharField(max_length=100,
                               widget=forms.TextInput(attrs={
                                   'class': 'form-control',
                                   'placeholder': 'Username',
                               })),
    password = forms.CharField(max_length=100,
                               widget=forms.TextInput(attrs={
                                   'class': 'form-control'
                               })),
    email = forms.CharField(max_length=100,
                            widget=forms.TextInput(attrs={
                                'class': 'form-control'
                            })),
    phone = forms.CharField(max_length=100,
                            widget=forms.TextInput(attrs={
                                'class': 'form-control'
                            }))
