from django.views.generic import (
    TemplateView,
)

from django_twitch_auth.views import TwitchLoginMixin


class HomeView(TemplateView):
    template_name = 'core/home.html'


class LoginView(TwitchLoginMixin, TemplateView):
    template_name = 'core/login.html'
