from django.db import models
from django.contrib.auth.models import User


class UserType(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    typpe= models.CharField(max_length=50)

    def __str__(self):
        return f"{0}||{1}".format(self.user, self.typpe)

