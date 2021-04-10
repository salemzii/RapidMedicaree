from django.shortcuts import render
from .forms import CreateAppointment
from .models import appointment
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib import messages
from django.views.generic import CreateView
import datetime
from datetime import time, date
from django.contrib.auth.decorators import login_required

@login_required()
def create_appointment(request, id):
    userr = User.objects.get(id=id)
    print(userr)

    if request.method == "POST":
        form = CreateAppointment(request.POST, instance=userr)
        if form.is_valid():
            time = form.cleaned_data.get('time')
            message = form.cleaned_data.get('message')
            patient = request.user
            #a = appointment.objects.create(doc=userr, time=form.cleaned_data.get('time'), message=form.cleaned_data.get('message'))
            doc_appointments = userr.doctor_appointment.all()

            for t in range(len(doc_appointments) + 1):
                print(str(time) == str(t))
                if str(time) == str(t):
                    messages.error(request, "Sorry This Time Slot Not Available! Try Another One")
                    pass
                else:
                    a = appointment.objects.create(doc=userr, time=form.cleaned_data.get('time'),
                                                   message=form.cleaned_data.get('message'))
            return redirect('verify')
    else:
        form = CreateAppointment()
    return render(request, 'userauth/createappointment.html', {'form': form})

