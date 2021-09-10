import requests

from django.contrib.auth.backends import BaseBackend
from django.contrib.auth import get_user_model
from django.conf import settings


User = get_user_model()


class TwitchBackend(BaseBackend):
    def authenticate(self, request, token=None):
        response = requests.get(
            settings.TWITCH_USERS_URL,
            headers={
                'Accept': 'application/vnd.twitchtv.v5+json',
                'Client-ID': settings.TWITCH_CLIENT_ID,
                'Authorization': f'Bearer {token}',
            }
        )
        if response.status_code == 200:
            user_informations = response.json()['data'][0]
            try:
                user = User.objects.get(username=user_informations['login'])
            except User.DoesNotExist:
                user_data = {
                    'username': user_informations['login'],
                    'email': user_informations['email'],
                }
                user = User.objects.create(**user_data)
            return user
        return None

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None
