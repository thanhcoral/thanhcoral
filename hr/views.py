from termcolor import colored

from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from django.http import HttpResponse
from django.template.loader import render_to_string
from django.contrib import messages
from django.contrib.auth.models import Group

from core import forms

from common.authorization import group_required, lv
from common.utils import html_to_pdf, get_time_now


@group_required('HR', raise_exception=True)
def users_list(request):
    users = get_user_model().objects.all()
    context = { 'users': users, }
    return render(request, 'hr/users-list.html', context)

@group_required('HR', raise_exception=True)
def users_add(request):
    form = forms.AddUserForm(request.POST or None)
    form2 = forms.UpdateProfileForm(request.POST or None)
    context = {
        'form': form,
        'form2': form2,
    }
    if request.method == 'POST':
        if form.is_valid():
            recent_group = request.user.groups.first().name
            request_group = form.cleaned_data.get('groups')
            print(colored(request_group, 'blue'))
            if lv(recent_group) >= lv(request_group):
                messages.warning(request, "You do not have permission add user at position:" + recent_group)
                context = {
                    'form': form,
                }
                return render(request, 'hr/users-add.html', context)

            user = form.save()
            group = Group.objects.get(name=request_group)
            user.groups.add(group)

            

            messages.success(request, "Succesful")
            return redirect('/hr/users-list')
        else:
            print(colored('form is not valid', 'red'))
    
    return render(request, 'hr/users-add.html', context)


@group_required('HR', raise_exception=True)
def staff_report(request):
    context = {
        'users': get_user_model().objects.all()
    }
    open('templates/temp.html', "w").write(render_to_string('reports/staff.html', context))
    pdf = html_to_pdf('temp.html')
    return HttpResponse(pdf, content_type='application/pdf')

