from django.urls import path
from . import views
#from .views import CreateAppointmentView

urlpatterns = [
    path('create-appointment/<int:id>', views.create_appointment, name='create-appointment'),
]