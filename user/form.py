from django import forms

from .models import User


class SubscriberForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['fist_name', 'last_name', 'phone_number', 'email']
