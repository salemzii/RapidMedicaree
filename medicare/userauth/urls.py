from django.urls import path
from . import views
from .views import verification
from django.contrib.auth import views as authviews


urlpatterns = [
    path('register/', views.register, name='register'),
    path('activate/<uidb64>/<token>', verification.as_view(), name='activate'),
    path('checkusertype/', views.show_form, name='checkuser'),
    path('login/', authviews.LoginView.as_view(template_name='userauth/login.html'), name='login'),
    path('logout/', authviews.LogoutView.as_view(template_name='userauth/logout.html'), name='logout'),
    path('verify/', views.verify, name='verify')
]

