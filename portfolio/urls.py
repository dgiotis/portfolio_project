from django.conf import settings
from django.conf.urls.static import static
from main import views
from django.urls import path
from django.contrib import admin
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
