from django import forms
from django.forms.models import ModelForm

from .models import PersonBiography


class PersonBiographyPluginForm(ModelForm):
    person = forms.ModelChoiceField(queryset=PersonBiography.active_objects.all())
