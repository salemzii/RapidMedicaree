from django import forms
from .models import appointment
from .slots import TUP_SLOTS, TIME_SLOTS
import pytz

time_slot = [

]

for time in TIME_SLOTS:
    time_slot.append(tuple([(pytz.utc.localize(time)), pytz.utc.localize(time)]))


class CreateAppointment(forms.ModelForm):
    time = forms.CharField(widget=forms.Select(choices=time_slot))
    message = forms.CharField(required=False, widget=forms.Textarea)

    class Meta:
        model = appointment
        fields = ['time', 'message']

