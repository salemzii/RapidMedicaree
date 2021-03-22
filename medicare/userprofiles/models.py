from django.db import models
from django.contrib.auth.models import User
from PIL import Image


class Userprofile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.CharField(max_length=150)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    address = models.CharField(max_length=101, default='Nigeria', blank=True, null=True)
    phoneNumber = models.CharField(max_length=11, default=123)
    age = models.IntegerField(default=2)

    def __str__(self):
        return f"{self.user.username}'s Profile"

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        img = Image.open(self.image.path)
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)


class Hospitalprofile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    AboutUs = models.CharField(max_length=150)
    verified = models.BooleanField(default=False)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    Address = models.CharField(max_length=101, default='Nigeria')
    phoneNumber = models.CharField(max_length=11, default= 123)
    license = models.ImageField(default = 'Document.png', upload_to='Documents')
    Frontview = models.ImageField(default='Hospital.jpg', upload_to='Hospital_pics')
    Backview = models.ImageField(default='Hospital.jpg', upload_to='Hospital_pics')
    rating = models.IntegerField(default= 0)


    def __str__(self):
        return f"{self.user.username}'s Profile"

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        img = Image.open(self.image.path)
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)

SPECTIALTIES = (
    ('Den', 'Dentist'),
    ('Pae', 'Peadetrician'),
    ('Car', 'Cardiologist'),
    ('Gyn', 'Gynacologist'),
    ('Doc', 'MedicalDoctor')
)

class Doctorprofile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.CharField(max_length=150)
    verified = models.BooleanField(default=False)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    homeAddress = models.CharField(max_length=101, default='Nigeria')
    phoneNumber = models.CharField(max_length=11, default= 123)
    doc_cert = models.ImageField(default = 'Document.png', upload_to='Documents')
    license = models.ImageField(default ='Document.png', upload_to='Documents')
    working_Hospital = models.CharField(max_length=150)
    about_doc = models.TextField(default='Tell us About yourself Doc!')
    specialty = models.CharField(max_length=100, default="Doc", choices=SPECTIALTIES)
    rating = models.IntegerField(default=0)
    consultation_fee = models.IntegerField(default=1000)

    def __str__(self):
        return f"{self.user.username}'s Profile"

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        img = Image.open(self.image.path)
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)

# Create your models here.
