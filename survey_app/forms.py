from django import forms
from .models import Survey
from django.contrib.auth.models import User

class SurveyForm(forms.ModelForm):
    class Meta:
        model = Survey
        fields = ['tea', 'coffee', 'biscuit', 'smoking']

class UserRegistrationForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email']