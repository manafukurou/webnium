from django import forms

class JobForm(forms.Form):
    job_name = forms.CharField(label='job_name', max_length=255)
    job_id = forms.CharField(label='job_id', max_length=255)