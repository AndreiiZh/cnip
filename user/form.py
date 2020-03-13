from django import forms
from django.contrib.gis.geoip2.resources import City
from mapwidgets.widgets import GooglePointFieldWidget, GoogleStaticOverlayMapWidget

from .models import User, Question


class SubscriberForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['fist_name', 'last_name', 'phone_number', 'email']


class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['fist_name', 'last_name', 'phone_number', 'email', 'question']
