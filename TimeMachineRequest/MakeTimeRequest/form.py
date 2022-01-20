from django.forms import ModelForm
from .models import Request
from django import forms

class DateTimeLocalInput(forms.DateTimeInput):
    input_type = "datetime-local"
    
class RequestForm(ModelForm):
    class Meta:
        model = Request
        fields = ['url','time_request']
        widgets = {
        'time_request': DateTimeLocalInput(attrs={'type': 'datetime-local'}),
        }