from django import forms

class JobForm(forms.Form):
    job_name = forms.CharField(label='job_name', max_length=255)
    CHOICE = [
        ('1', 'data_1'),
        ('2', 'data_2'),
        ('3', 'data_3')]
    sample_select = forms.ChoiceField(
        label="sample_select",
        required=True,
        disabled=False,
        initial=['2'],
        choices=CHOICE,
        widget=forms.Select(attrs={
            'id': 'one', }))
    sample_radio = forms.ChoiceField(
        label='sample_radio',
        widget=forms.RadioSelect,
        choices=CHOICE,
        initial=0)

    sample_int = forms.IntegerField()

    sample_comment = forms.CharField(widget=forms.Textarea)