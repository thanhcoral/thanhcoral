from termcolor import colored

from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from django.http import HttpResponse
from django.template.loader import render_to_string
from django.contrib import messages
from django.contrib.auth.models import Group

from core import forms
from hr import models

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
        if form.is_valid() and form2.is_valid():
            recent_group = request.user.groups.first().name
            request_group = form.cleaned_data.get('groups')
            print(colored(request_group, 'blue'))
            if lv(recent_group) >= lv(request_group):
                messages.warning(request, "You do not have permission add user at position:" + recent_group)
                context = {
                    'form': form,
                }
                return redirect('/hr/users-add')

            user = form.save()
            group = Group.objects.get(name=request_group)
            user.groups.add(group)

            target_user = get_user_model().objects.get(id=user.id)
            profile_form = forms.UpdateProfileForm(request.POST, request.FILES, instance=target_user.profile)
            profile_form.save()


            messages.success(request, "Succesful")
            return redirect('/hr/users-list')
        else:
            print(colored('form is not valid', 'red'))
    
    return render(request, 'hr/users-add.html', context)

@group_required('HR', raise_exception=True)
def users_delete(request, pk):
    try:
        user = get_user_model().objects.get(id=pk)
    except:
        messages.warning(request, "User not exist")
        return redirect('/hr/users-list')
    get_user_model().objects.filter(id=pk).delete()
    messages.success(request, "Delete successfully")
    return redirect('/hr/users-list')

@group_required('HR', raise_exception=True)
def users_edit(request, pk):
    target_user = get_user_model().objects.get(id=pk)
    if request.method == 'POST':
        form = forms.UpdateUserForm(request.POST, instance=target_user)
        form2 = forms.UpdateProfileForm(request.POST, request.FILES, instance=target_user.profile)

        if form.is_valid() and form2.is_valid():
            form.save()
            form2.save()
            messages.success(request, 'Your profile is updated successfully')
            return redirect(f"/hr/users-edit/{pk}")
    else:
        form = forms.UpdateUserForm(instance=target_user)
        form2 = forms.UpdateProfileForm(instance=target_user.profile)

    return render(request, 'hr/users-edit.html', {'target_user': target_user, 'form': form, 'form2': form2})

@group_required('HR', raise_exception=True)
def staff_report(request):
    context = {
        'users': get_user_model().objects.all()
    }
    open('templates/temp.html', "w").write(render_to_string('reports/staff.html', context))
    pdf = html_to_pdf('temp.html')
    return HttpResponse(pdf, content_type='application/pdf')


