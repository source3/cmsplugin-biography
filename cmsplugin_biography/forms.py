from django import forms
from django.forms.models import ModelForm

from .models import PersonBiography


class PersonBiographyPluginForm(ModelForm):
    person = forms.ModelChoiceField(queryset=PersonBiography.objects.filter(active=True))

    class Meta:
        model = PersonBiography
