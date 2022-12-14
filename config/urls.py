from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.views import LogoutView

from django.conf import settings
from django.conf.urls.static import static

from core import views as core_views, forms
from hr import views as hr_views

urlpatterns = [
    # django-admin-site
    path('admin/', admin.site.urls),

    # auth
    path('login', core_views.LoginView.as_view(redirect_authenticated_user=True, template_name='auth/login.html', authentication_form=forms.LoginForm), name='login'),
    path('logout', LogoutView.as_view(template_name='auth/logout.html'), name='logout'),
    path('checkin', core_views.checkin, name='checkin'),
    path('checkout', core_views.checkout, name='checkout'),
    path('timesheet', core_views.timesheet, name='timesheet'),

    path('', core_views.index, name='home'),
    path('dashboard', core_views.dashboard, name='dashboard'),

    path('hr/users-list', hr_views.users_list, name='users-list'),
    path('hr/users-add', hr_views.users_add, name='users-add'),
    path('hr/users-edit/<int:pk>', hr_views.users_edit, name='users-edit'),
    path('hr/users-delete/<int:pk>', hr_views.users_delete, name='users-delete'),
    path('hr/staff-report', hr_views.staff_report, name='staff-report'),
    



] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

