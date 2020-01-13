from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Profile, Comments, Ocenka
from django.contrib.auth import get_user_model
User = get_user_model()


class DoctorLoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class DoctorRegisterForm(forms.ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repeat Password', widget=forms.PasswordInput)

    class Meta:
        model = Profile
        fields = ['username','first_name','last_name', 'clinic', 'type']

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Passwords do not match.')
        return cd['password2']


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ['nickname', 'text' ]


class EvaluationForm(forms.ModelForm):
    class Meta:
        model = Ocenka
        fields = ['ocenka']
