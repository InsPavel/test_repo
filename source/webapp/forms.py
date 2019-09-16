from django import forms
from django.forms import widgets
from webapp.models import STATUS_CHOICES


class DateInput(forms.DateInput):
    input_type = 'date'


class IssueForm(forms.Form):
    description = forms.CharField(max_length=200, required=True, label='Description')
    status = forms.ChoiceField(choices=STATUS_CHOICES, initial=STATUS_CHOICES[0][0], required=True, label='Status')
    finish_date = forms.DateField(required=False, initial='', label='Finish_date', widget=DateInput)
