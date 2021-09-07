from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', include('universo_nextlevel.core.urls')),
    path('admin/', admin.site.urls),
    path('personagem/', include('universo_nextlevel.personagem.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
