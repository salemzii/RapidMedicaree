from django.urls import path
from . import views


urlpatterns = [
    path('friend-list/', views.friends, name='friends'),
    path('doctors-list/', views.doctors, name='doctors'),
    path('hospitals-list/', views.hospitals, name='hospitals'),
    path('pharmacies-list/', views.pharmacies, name='pharmacies'),
    path('userupdateprofile/>', views.userupdateform, name='userupdate'),
    path('doctorupdateprofile/', views.doctorupdateform, name='doctorupdate'),
    path('hospitalupdateprofile/', views.hospitalupdateform, name='hospitalupdate'),
    path('pharmacyupdateprofile/', views.pharmacyupdateform, name='pharmacyupdate'),
    path('profileView/<int:id>/', views.userprofileview, name='userprofileview'),
    path('docprofileView/<int:id>/', views.doctorprofileview, name='doctorprofileview'),
    path('hospitalprofileView/<int:id>/', views.hospitalprofileview, name='hospitalprofileview'),
    path('pharmprofileView/<int:id>/', views.pharmacyprofileview, name='pharmacyprofileview'),
]

