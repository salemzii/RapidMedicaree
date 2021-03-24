from django.shortcuts import render
from .forms import CreateAppointment
from .models import appointment
from django.contrib.auth.models import User
from django.shortcuts import render, redirect



def create_appointment(request, id):
    userr = User.objects.get(id=id)
    if request.method == "POST":
        form = CreateAppointment(request.POST, instance=userr)
        if form.is_valid():
            time = form.cleaned_data.get('time')
            message = form.cleaned_data.get('message')
            patient = request.user
            form.save()
            return redirect('verify')
    else:
        form = CreateAppointment()
    return render(request, 'userauth/createappointment.html', {'form': form})





























