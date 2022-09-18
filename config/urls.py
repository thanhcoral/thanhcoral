from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

from apps.core import views as core_views
from apps.authentication import views as auth_views


urlpatterns = [
    path('admin/', admin.site.urls),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


urlpatterns += [
    path('', core_views.home, name='home'),
]