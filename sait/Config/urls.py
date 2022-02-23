from django.contrib import admin
from django.urls import path, include #include napravliaet na drugie urladressa

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    path('news/', include('news.urls')),
    path('newsportal/', include('newsportal.urls'))
] +static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
