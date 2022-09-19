from django.shortcuts import render
from django.contrib.auth import get_user_model

from common.authorization import group_required


@group_required('HR', raise_exception=True)
def user_list(request):
    users = get_user_model().objects.all()
    context = { 'users': users, }
    return render(request, 'hr/users-list.html', context)