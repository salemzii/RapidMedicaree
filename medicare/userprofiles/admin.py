from django.contrib import admin
from .models import Userprofile, Doctorprofile, Hospitalprofile
from django.contrib.auth.models import User



@admin.register(Userprofile)
class Custom(admin.ModelAdmin):
    list_display = ['user', 'user_mail', 'user_id']

    def user_id(self, obj):
        u = User.objects.get(username=obj.user.username)
        return u.id

    def user_mail(self, obj):
        u = User.objects.get(username=obj.user.username)
        return u.email


@admin.register(Doctorprofile)
class Custom(admin.ModelAdmin):
    list_display = ['user', 'user_mail', 'user_id']

    def user_id(self, obj):
        u = User.objects.get(username=obj.user.username)
        return u.id

    def user_mail(self, obj):
        u = User.objects.get(username=obj.user.username)
        return u.email


@admin.register(Hospitalprofile)
class Custom(admin.ModelAdmin):
    list_display = ['user', 'user_mail', 'user_id']

    def user_id(self, obj):
        u = User.objects.get(username=obj.user.username)
        return u.id

    def user_mail(self, obj):
        u = User.objects.get(username=obj.user.username)
        return u.email