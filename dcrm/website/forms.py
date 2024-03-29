from typing import Any
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class SignupForm(UserCreationForm):
    email = forms.EmailField( label= "", widget=forms.TextInput(attrs={'class': 'forms-control', 'placeholder': 'Email Address'}))
    first_name = forms.CharField( label= "",max_length="100", widget=forms.TextInput(attrs={'class': 'forms-control', 'placeholder': 'First Name'}))
    last_name = forms.CharField( label= "",max_length="100", widget=forms.TextInput(attrs={'class': 'forms-control', 'placeholder': 'Last Name'}))

    class Meta:
        model = User
        fields = ('Username', 'first_name', 'last_name', 'email', 'password1', 'password2')
    
    def __init__(self, *args: Any, **kwargs):
        super(SignupForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['placeholder'] = 'User Name'
        self.fields['username'].label = ''
        self.fields['username'].help_text = '<span class = "form-text text-muted"><small>Required. 150 characters or fewer. letters or digits and @/./+/-/_only.</small></span>'
        
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['placeholder'] = 'Password'
        self.fields['Password1'].label = ''
        self.fields['password1'].help_text = '<span class = "form-text text-muted small"><li>Your password can\'t be too similar to your other personal information.</li><li>Your password must contain at least 8 characters.</li><li>Your password can\'t be a commonly used password.</li><li>Your password can\'t be entirely numeric.</li></ul>'
        
        self.fields['password2'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['placeholder'] = 'Confirm Password'
        self.fields['password2'].label = ''
        self.fields['password2'].help_text = '<span class = "form-text text-muted"><small>Enter the same password as before, for verification.</small></span>'