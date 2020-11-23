from django import forms

class PartsForm(forms.Form):
    parts_name = forms.CharField(label='parts_name', max_length=200)
    description = forms.CharField(label='description', max_length=255)
    parts_id = forms.CharField(label='pars_id', max_length=255)