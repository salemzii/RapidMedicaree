from django import forms
from .models import Userprofile, Doctorprofile, Hospitalprofile, Pharmacyprofile


class UserProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Userprofile
        fields = ['bio', 'image', 'address', 'phoneNumber', 'age']


class DoctorProfileUpdateForm(forms.ModelForm):

    class Meta:
        model = Doctorprofile
        fields = ['bio', 'image', 'homeAddress',
                  'phoneNumber', 'doc_cert', 'license', 'working_Hospital',
                  'about_doc', 'specialty', 'consultation_fee']


class HospitalProfileUpdateForm(forms.ModelForm):

    class Meta:
        model = Hospitalprofile
        fields = ['image', 'phoneNumber', 'Address', 'AboutUs',
                  'license', 'Frontview', 'Backview']



class PharmacyProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Pharmacyprofile
        fields = [
            'bio', 'image', 'phoneNumber', 'license', 'specialty'
        ]
