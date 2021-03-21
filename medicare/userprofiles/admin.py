from django.contrib import admin
from .models import Userprofile, Doctorprofile, Hospitalprofile


admin.site.register(Userprofile)
admin.site.register(Doctorprofile)
admin.site.register(Hospitalprofile)