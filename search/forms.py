from django import forms

from .choices import *


class SearchForm(forms.Form):
    woman = forms.ChoiceField(widget=forms.Select, choices=WOMAN_CHOICES, label='')
    occasion = forms.ChoiceField(widget=forms.Select, choices=OCCASION_CHOICES, label='')
    price = forms.ChoiceField(widget=forms.Select, choices=PRICE_CHOICES, label='', required=False)
