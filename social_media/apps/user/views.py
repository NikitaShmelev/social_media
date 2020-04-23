from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from django.contrib.auth.models import User
from django.core.mail import EmailMessage
from django.utils.datastructures import MultiValueDictKeyError
from django.conf import settings

from os import path

from .models import UserProfile

from .tokens import account_activation_token
from .forms import SignupForm



def index(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect('../../home')
    else:
        return HttpResponseRedirect('../../home')


def sign_in(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect(f'../../user/profile/{user.id}')
                # return render(request, 'profile_page.html', {'profile_id': user.id})
            return render(request, 'sign_in.html')
        else:
            return render(request, 'sign_in.html')
    else:
        return HttpResponseRedirect('../../home')


def register(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            current_site = get_current_site(request)
            mail_subject = 'Activate your blog account.'
            message = render_to_string('acc_active_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid':urlsafe_base64_encode(force_bytes(user.pk)),
                'token':account_activation_token.make_token(user),
            })
            to_email = form.cleaned_data.get('email')
            email = EmailMessage(
                        mail_subject, message, to=[to_email]
            )
            email.send()
            return HttpResponse('Please confirm your email address to complete the registration')
    else:
        form = SignupForm()
    return render(request, 'sign_up.html', {'form': form})


def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        profile = UserProfile(
            user=user,
            profile_id=user.id,
        )
        profile.save_base()
        login(request, user)
        HttpResponseRedirect(f'../../user/profile/{user.id}')
    else:
        return HttpResponse('Activation link is invalid!')


def show_profile(request, profile_id):
    try:
        profile = UserProfile.objects.get(profile_id=profile_id)
    except:
        raise Http404('Page not found(')

    return render(request, 'profile_page.html', {
        'profile': profile,
        })


def edit_profile(request, profile_id):
    if request.method == 'POST':
        try:
            avatar = request.FILES['profile_img']
            path_to_save = f'{settings.MEDIA_ROOT}/profile_image/{avatar}'
            with open(path_to_save, 'wb+') as f:
                for chunk in avatar.chunks():
                    f.write(chunk)
            UserProfile.objects.filter(profile_id=profile_id).update(
                first_name=request.POST['first_name'],
                second_name=request.POST['second_name'],
                bio=request.POST['bio'],
                avatar=f'profile_image/{avatar}',
            )
        except MultiValueDictKeyError:
            UserProfile.objects.filter(profile_id=profile_id).update(
                first_name=request.POST['first_name'],
                second_name=request.POST['second_name'],
                bio=request.POST['bio'],
                )
    return HttpResponse('EDIT')
