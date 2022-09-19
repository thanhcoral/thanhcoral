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

    path('', core_views.index, name='home'),
    path('dashboard', core_views.dashboard, name='dashboard'),

    path('hr/users-list', hr_views.user_list, name='users-list')




] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

