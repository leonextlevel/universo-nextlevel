from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from .views import HomeView, LoginView, twitch_authorize
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('authorize/', twitch_authorize, name="twitch_authorize"),
]
