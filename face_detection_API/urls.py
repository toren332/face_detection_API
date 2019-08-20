from django.conf.urls import url
from django.contrib import admin
from django.urls import include, path
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^api/v1/', include('api_v1.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)