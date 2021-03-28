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


def friends(request):
    useradress = str(request.user.userprofile.address)
    friendsadress = Userprofile.objects.all()

    friends_list = [
        friendadress.user for friendadress in friendsadress if str(useradress) == friendadress.address
    ]

    print(friends_list)

    return render(request, 'userauth/friends.html', {'friends_list': friends_list})


def doctors(request):
    useradress = str(request.user.userprofile.address)
    doctorsaddress = Doctorprofile.objects.all()

    doctors = [
        doctoraddress.user for doctoraddress in doctorsaddress if str(useradress) == doctoraddress.homeAddress
    ]
    return render(request, 'userauth/doctors.html', {'doctors': doctors})


def hospitals(request):
    useradress = str(request.user.userprofile.address)
    hospitalsaddress = Hospitalprofile.objects.all()

    hospitals = [
        hospitaladdress.user for hospitaladdress in hospitalsaddress if str(useradress) == hospitaladdress .Address
    ]
    return render(request, 'userauth/hospitals.html', {'hospitals': hospitals})

# Create your views here.

