from django.shortcuts import (
                                render,
                              redirect,
                              get_object_or_404
)
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm #UserUpdateForm #ProfileUpdateForm
from django.utils.encoding import (
                                    force_bytes,
                                   force_text,
                                   DjangoUnicodeDecodeError
)
from django.utils.http import (
                                urlsafe_base64_encode,
                               urlsafe_base64_decode
)
from django.contrib.sites.shortcuts import get_current_site
from .utils import account_activation_token
from django.contrib.auth.models import User
from django.views.generic import View
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.mail import send_mail
from userprofiles.models import (Userprofile,
                                 Doctorprofile,
                                 Hospitalprofile,
                                Pharmacyprofile,
)
from .models import UserType



#User registration
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            mail = form.cleaned_data.get('email')
            number = form.cleaned_data.get('phoneNumber')
            form.save()

            userr = User.objects.get(username=username)

            userr = User.objects.get(username=username)
            if len(str(number)) > 9:
                userr.is_active = True
                userr.save()


            uidb64 = urlsafe_base64_encode(force_bytes(userr.pk))

            domain = get_current_site(request).domain
            link = reverse('activate', kwargs={'uidb64': uidb64, 'token': account_activation_token.make_token(userr)})
            activate_url = 'http://' + domain + link
            email_subject = 'Activate your account'
            email_body = 'Hello {0} thanks for signing up with us, please use this link to verify your account \n {1}'.format(
                username, activate_url)

            email = send_mail(email_subject, email_body, 'Noreply@FX.com', [mail], fail_silently=True)
            messages.success(request, f'Congrats {username}, Your account was created successfully')

            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'userauth/register.html', {'form': form})


#verify user email
class verification(View):
    def get(self, request, uidb64, token):

        try:
            id = force_text(urlsafe_base64_decode(uidb64))
            user = User.objects.get(pk=id)

            if not account_activation_token.check_token(user, token):
                return redirect('login' + '?message' + 'User already activated')
            #if user.is_active:
            #    return redirect('login')
            #user.is_active = True
            #user.save()

            messages.success(request, 'Account activated successfully')
            return redirect('login')
        except Exception as e:
            pass
        return redirect('login')


# check user type, Patient, doctor/consultant, or hospital
def show_form(request):
    print('this function has been called')
    print(request.user)
    val = ''

    try:
        u_prof = Userprofile.objects.get(user=request.user)
        if u_prof:
            return redirect(reverse('userprofileview', args=[u_prof.user.id]))
    except Exception as e:
        pass

    try:
        d_prof = Doctorprofile.objects.get(user=request.user)
        if d_prof:
            return redirect(reverse('userprofileview', args=[d_prof.user.id]))
    except Exception as e:
        pass

    try:
        h_prof = Hospitalprofile.objects.get(user=request.user)
        if h_prof:
            return redirect(reverse('hospitalprofileview', args=[h_prof.user.id]))
    except Exception as e:
        pass

    try:
        p_prof = Pharmacyprofile.objects.get(user=request.user)
        if p_prof:
            return redirect(reverse('pharmacyprofileview', args=[p_prof.user.id]))
    except Exception as e:
            pass

    if request.method == "POST":
        val = request.POST['choice']
        try:
            if val == "Patient":
                prof = Userprofile.objects.create(user=request.user)
                u_type = UserType.objects.create(user=request.user, typpe=val)
                u_type.save()
                prof.save()
            elif val == "Doctor/Consultant":
                prof = Doctorprofile.objects.create(user=request.user)
                u_type = UserType.objects.create(user=request.user, typpe=val)
                u_type.save()
                prof.save()
            elif val == "Hospital":
                profile = Hospitalprofile.objects.create(user=request.user)
                u_type = UserType.objects.create(user=request.user, typpe=val)
                u_type.save()
                profile.save()

            elif val == "Pharmacy":
                profile = Pharmacyprofile.objects.create(user=request.user)
                u_type = UserType.objects.create(user=request.user, typpe=val)
                u_type.save()
                profile.save()

        except Exception as e:
            print("Something interuppted the process... ")
    return render(request, 'userauth/checkusertype.html', {'request': request})


def verify(request):
    pr=request.user
    print(pr)
    return render(request, 'userauth/verify.html', {'vr':pr})
