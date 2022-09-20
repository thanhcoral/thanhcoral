import datetime
from time import strftime, gmtime
from calendar import monthrange


from django.utils import timezone
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import ListView
from django.contrib import messages
from django.contrib.auth.views import LoginView
from django.contrib.auth.models import Group
from django.contrib.auth.decorators import login_required

from core.forms import LoginForm
from hr import models

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


@login_required
def checkin(request):
    year, month, day = get_time_now()
    models.TimeSheet.objects.get_or_create(user=request.user, year=year, month=month, day=day)
    return redirect('/')

@login_required
def checkout(request):
    year, month, day = get_time_now()
    try:
        timesheet = models.TimeSheet.objects.get(user=request.user, year=year, month=month, day=day)
    except:
        messages.warning(request, 'checkin before')
        return redirect('/')
    timesheet.checkout = timezone.now()

    # timesheet.checkin = datetime.datetime(2022,9,14,7,58,20,123456)
    # timesheet.checkout = datetime.datetime(2022,9,14,18,14,25,123456)

    checkin = timesheet.checkin
    checkout = timesheet.checkout

    if (checkin - datetime.datetime(year,month,day,8,0,0,0)).days > 0 :
        timesheet.late = (checkin - datetime.datetime(year,month,day,8,0,0,0)).seconds

    if (datetime.datetime(year,month,day,17,0,0,0) - checkout).days < 0:
        timesheet.ot = (checkout - datetime.datetime(year,month,day,17,0,0,0)).seconds

    a = range(1, monthrange(year, month)[1]+1) 
    if (day == a[-1]):
        try:
            salary = models.Salary.objects.get(user=request.user)
        except:
            models.Salary.objects.filter(user=request.user).delete()
            models.Salary.objects.create(user=request.user)
    
    timesheet.time = (checkout - checkin).seconds
    timesheet.save()
    # print( strftime("%H:%M:%S", gmtime(timesheet.time)) )
    return redirect('/')

