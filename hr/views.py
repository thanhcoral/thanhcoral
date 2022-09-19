from django.shortcuts import render
from django.contrib.auth import get_user_model
from django.http import HttpResponse
from django.template.loader import render_to_string


from common.authorization import group_required
from common.utils import html_to_pdf, get_time_now


@group_required('HR', raise_exception=True)
def user_list(request):
    users = get_user_model().objects.all()
    context = { 'users': users, }
    return render(request, 'hr/users-list.html', context)

@group_required('HR', raise_exception=True)
def staff_report(request):
    context = {
        'users': get_user_model().objects.all()
    }
    open('templates/temp.html', "w").write(render_to_string('reports/staff.html', context))
    pdf = html_to_pdf('temp.html')
    return HttpResponse(pdf, content_type='application/pdf')

