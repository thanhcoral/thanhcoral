
from django.utils import timezone
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import ListView
from django.contrib import messages
from django.contrib.auth.views import LoginView
from django.contrib.auth.models import Group
from django.contrib.auth.decorators import login_required

from core.forms import RegisterForm, LoginForm, AddUserForm, UpdateProfileForm

from common.authorization import group_required, lv
from common.utils import get_time_now


class LoginView(LoginView):
    form_class = LoginForm
    def form_valid(self, form):
        remember_me = form.cleaned_data.get('remember_me')
        if not remember_me:
            self.request.session.set_expiry(0)
            self.request.session.modified = True
        return super(LoginView, self).form_valid(form)

@login_required
def index(request):
    return render(request, 'index.html')

@login_required
def dashboard(request):
    return render(request, 'dashboard.html')