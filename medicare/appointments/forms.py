from django import forms
from .models import appointment

class CreateAppointment(forms.ModelForm):
    time = forms.DateTimeField()
    message = forms.CharField(required=False)

    class Meta:
        model = appointment
        fields = ['time', 'message']
