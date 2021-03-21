from django.urls import path
from . import views


urlpatterns = [
    path('userupdateprofile/>', views.userupdateform, name='userupdate'),
    path('doctorupdateprofile/', views.doctorupdateform, name='doctorupdate'),
    path('hospitalupdateprofile/', views.hospitalupdateform, name='hospitalupdate'),
    path('profileView/<int:id>/', views.userprofileview, name='userprofileview'),
    path('docprofileView/<int:id>/', views.doctorprofileview, name='doctorprofileview'),
    path('hospitalprofileView/<int:id>/', views.hospitalprofileview, name='hospitalprofileview'),
]

