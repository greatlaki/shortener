from django import forms

from .models import *


class UrlForm(forms.ModelForm):

    long_url = forms.URLField(widget=forms.URLInput(
        attrs=
        {
            "class": "url-form",
            "placeholder": "Введите URL"
        }
    ))

    class Meta:
        model = Urls
        fields = ['long_url', 'author']
