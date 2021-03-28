from django.shortcuts import render
from .forms import CreateAppointment
from .models import appointment
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib import messages
from django.views.generic import CreateView
import datetime
from datetime import time, date


def create_appointment(request, id):
    userr = User.objects.get(id=id)
    print(userr)

    if request.method == "POST":
        form = CreateAppointment(request.POST, instance=userr)
        if form.is_valid():
            time = form.cleaned_data.get('time')
            message = form.cleaned_data.get('message')
            patient = request.user
            a = appointment.objects.create(doc=userr, time=form.cleaned_data.get('time'), message=form.cleaned_data.get('message'))
            doc_appointments = userr.doctor_appointment.all()
            print(a.time)
            for time in range(len(doc_appointments)):
                print(a.time == time)
                if a.time != time:
                    messages.error(request, "Time Slot Not Available! Try again")
                    break
                else:
                    pass
            return redirect('verify')
    else:
        form = CreateAppointment()
    return render(request, 'userauth/createappointment.html', {'form': form})





"""
class CreateAppointmentView(CreateView):
    model = appointment
    context_object_name = 'form'
    template_name = 'userauth/createappointment.html'
    form_class = CreateAppointment
    pk_url_kwarg = 'id'

"""