from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    path('vivod/', include('vivod.urls')),
    path(r'^favicon\.ico$', RedirectView.as_view(url='/static/main/pictures/favicon.ico', permanent=True)),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
