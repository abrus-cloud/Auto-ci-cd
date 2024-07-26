from django.shortcuts import render, redirect
import json
from requests import Request, Session
from requests_oauthlib import OAuth1
from .forms import Regisrtration, EditProfile
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import PasswordChangeForm, PasswordResetForm, AuthenticationForm
from django.contrib.auth import update_session_auth_hash, login, logout, authenticate
from django.template.loader import render_to_string
from django.db.models.query_utils import Q
from django.utils.http import urlsafe_base64_encode
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes
from django.contrib.auth.models import User
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required



def login_redirect(request):
    if request.user.is_authenticated:
        return redirect('/home')
    return redirect('/login')


def password_reset_request(request):
    if request.method == "POST":
        password_reset_form = PasswordResetForm(request.POST)
        if password_reset_form.is_valid():
            data = password_reset_form.cleaned_data['email']
            associated_users = User.objects.filter(Q(email=data))
            if associated_users.exists():
                for user in associated_users:
                    subject = "Password Reset Requested"
                    email_template_name = "Make_API/password/ password_reset_email.txt"
                    c = {
                        "email": user.email,
                        'domain': '127.0.0.1:8000',
                        'site_name': 'Flying Cloud',
                        "uid": urlsafe_base64_encode(force_bytes(user.pk)),
                        "user": user,
                        'token': default_token_generator.make_token(user),
                        'protocol': 'http',
                    }
                    email = render_to_string(email_template_name, c)
                    try:
                        send_mail(subject, email, 'admin@example.com', [user.email], fail_silently=False)
                    except BadHeaderError:
                        return HttpResponse('Invalid header found.')
                    return redirect("/password_reset/done/")
    password_reset_form = PasswordResetForm()
    return render(request=request, template_name="Make_API/password/password_reset.html",
                  context={"password_reset_form": password_reset_form})


@login_required()
def home_page(request):
    return render(request, 'adminlte/base.html')


@login_required()
def logout_request(request):
    logout(request)
    messages.success(request, "Loged out successfuly")
    return render(request, 'Make_API/logout.html')


def login_request(request):
    if request.user.is_authenticated:
        return redirect('/home')
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                if 'next' in request.POST:
                    return redirect(request.POST.get('next'))

                messages.info(request, f'You are now logged in as {username}')
                return redirect('/home')
            else:
                messages.error(request, 'Invalid username or password')
        else:
            messages.error(request, 'Invalid username or password')
    form = AuthenticationForm()
    args = {'form': form}
    return render(request=request, template_name='Make_API/login.html', context=args)


class UserLogin(LoginView):
    template_name = 'Make_API/login.html'


class UserLogOut(LogoutView):
    template_name = "Make_API/logout.html"


@login_required()
def create_instance(request):
    if request.method == 'POST':
        cpu_cores = request.POST['cpu_cores']
        memory_os = request.POST['memory']
        get_hostname = request.POST['get_hostname']
        auth1 = OAuth1(u'txDqESa7F7fSFqccSX', u'',
                       u'C4AhG4AmAEkTqEF55a', u'2gbTjNrYfPDbYyFqBp3acMd2NQySGajr')
        headers = {'Accept': 'application/json'}
        url = u'http://172.18.34.245:5240/MAAS/api/2.0/pods/1/?op=compose'
        body = json.dumps({
            'cores': cpu_cores,
            'memory': memory_os,
            'hostname': get_hostname,
        })
        headers = {'Content-Type': 'application/json', }
        s = Session()
        req = Request('POST', url, headers=headers, auth=auth1, data=body)
        prepped = req.prepare()
        resp = s.send(prepped)
        out_put = {'sys_id': resp.text, }
        messages.success(request, 'Your instance Created')
    return render(request, 'adminlte/create_instance.html')


@login_required()
def get_machine_info(request):
    pass


def register(request):
    if request.method == 'POST':
        form = Regisrtration(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Your registration was successful")
            return redirect('/home')
        messages.error(request, "Unsuccessful registration. Invalid information.")

    form = Regisrtration()
    args = {'form': form}
    return render(request, 'registration/register.html', args)


@login_required
def view_profile(request):
    args = {'user': request.user}
    return render(request, "Make_API/view_profile.html", args)


@login_required
def edit_profile(request):
    if request.method == "POST":
        form = EditProfile(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profie updated')
            return redirect('/home/profile')
        messages.error(request, 'Operations Failed')
    else:
        form = EditProfile(instance=request.user)
        args = {'form': form}
        return render(request, 'Make_API/edit_profile.html', args)


@login_required
def change_password(request):
    if request.method == "POST":
        form = PasswordChangeForm(data=request.POST, user=request.user)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, user=form.user)
            messages.success(request, 'Your Password has Changed')
            return redirect('/home/profile')
        messages.error(request, 'Your password does not change')
        return redirect('/change-password')
    else:
        form = PasswordChangeForm(user=request.user)
        args = {'form': form}
        return render(request, 'Make_API/edit_profile.html', args)


def test(request):
    list_of_users = [1, 2, 3, 4, 5, 6]
    name = 'yashar'
    args = {
        'myname': name,
        'user_list': list_of_users,
    }
    return render(request, 'Make_API/index.html', args)
