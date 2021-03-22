from django import forms
from .models import Userprofile, Doctorprofile, Hospitalprofile


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


"""
    AboutUs = models.CharField(max_length=150)
    verified = models.BooleanField(default=False)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    Address = models.CharField(max_length=101, default='Nigeria')
    phoneNumber = models.CharField(max_length=11, default= 123)
    license = models.ImageField(default = 'Document.png', upload_to='Documents')
    Frontview = models.ImageField(default='Hospital.jpg', upload_to='Hospital_pics')
    Backview = models.ImageField(default='Hospital.jpg', upload_to='Hospital_pics')
    rating = models.IntegerField(default= 0)
"""