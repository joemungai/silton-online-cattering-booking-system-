from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Package


class RegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['email', 'username', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super(RegisterForm, self).__init__(*args, **kwargs)

        for field in ['email', 'username', 'password1', 'password2']:
            self.fields[field].help_text = None


class PackageForm(forms.ModelForm):
    class Meta:
        model = Package
        fields = '__all__'
