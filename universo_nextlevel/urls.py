from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', include('universo_nextlevel.core.urls')),
    path('django_twitch_auth/', include('django_twitch_auth.urls')),
    path('admin/', admin.site.urls),
    path('personagem/', include('universo_nextlevel.personagem.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
