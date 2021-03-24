from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import datetime
from .slots import TUP_SLOTS, TIME_SLOTS



time_slot = [

]


for time in TIME_SLOTS:
    time_slot.append(tuple([(time), time]))



class appointment(models.Model):
    doc = models.ForeignKey(User, on_delete=models.CASCADE, related_name="doc")
    time = models.DateTimeField(choices=time_slot)
    message = models.TextField(null=True, blank=True)
    approved = models.BooleanField(default=False)
    time.editable = True

    def __str__(self):
        return str(self.time.time())



# Create your models here.
