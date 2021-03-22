from django.shortcuts import render, redirect, get_object_or_404, reverse
from .models import Userprofile, Doctorprofile, Hospitalprofile
from .forms import UserProfileUpdateForm, DoctorProfileUpdateForm, HospitalProfileUpdateForm
from django.contrib import messages
from django.views.generic import UpdateView
from django.contrib.auth.models import User


def userupdateform(request):
    userr = Userprofile.objects.get(user=request.user)
    print(request.user)
    if request.method == "POST":
        updateform = UserProfileUpdateForm(request.POST, request.FILES, instance=userr)
        if updateform.is_valid():
            updateform.save()
            messages.success(request, f'Account Update Successful!')
            return redirect('verify')
    else:
        updateform = UserProfileUpdateForm(instance=userr)

    context = {'form': updateform}
    return render(request, 'userauth/userprofileUpdate.html', context)


def doctorupdateform(request):
    doctor = Doctorprofile.objects.get(user=request.user)
    print(request.user)
    if request.method == "POST":
        updateform = DoctorProfileUpdateForm(request.POST, request.FILES, instance=doctor)
        if updateform.is_valid():
            updateform.save()
            messages.success(request, f'Account Update Successful!')
            return redirect('verify')
    else:
        updateform = DoctorProfileUpdateForm(instance=doctor)

    context = {'form': updateform}
    return render(request, 'userauth/doctorprofileupdate.html', context)


def hospitalupdateform(request):
    hospital = Hospitalprofile.objects.get(user=request.user)
    if request.method == "POST":
        updateform = HospitalProfileUpdateForm(request.POST, request.FILES, instance=hospital)
        if updateform.is_valid():
            updateform.save()
            messages.success(request, f'Account Update Successful!')
            return redirect('verify')
    else:
        updateform = HospitalProfileUpdateForm(instance=hospital)

    context = {'form': updateform}
    return render(request, 'userauth/hospitalprofileupdate.html', context)


def userprofileview(request, id):
    userr = User.objects.get(id=id)
    try:

        if userr.doctorprofile:
            return redirect(reverse('doctorprofileview', args=[id]))
        if userr.hospitalprofile:
            return redirect(reverse('hospitalprofileview', args=[id]))
    except Exception as e:
        print('Does not exist')

    context = {'user': userr}
    return render(request, 'userauth/userprofile.html', context)


def doctorprofileview(request, id):
    doc = User.objects.get(id=id)
    context = {'user': doc}
    return render(request, 'userauth/docprofile.html', context)


def hospitalprofileview(request, id):
    hos = User.objects.get(id=id)
    context = {'user': hos}
    return render(request, 'userauth/hosprofile.html', context)

# Create your views here.