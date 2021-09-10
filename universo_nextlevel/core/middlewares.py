import requests

from django.conf import settings


class TwitchAuthenticationMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        try:
            token = request.session['access_token']
            validate_response = requests.get(settings.TWITCH_TOKEN_VALIDATE, headers={
                'Authorization': f'Bearer {token}'
            })
            if validate_response.status_code != 200:
                refresh_token = request.session['refresh_token']
                token_params = {
                    'client_id': settings.TWITCH_CLIENT_ID,
                    'client_secret': settings.TWITCH_CLIENT_SECRET,
                    'refresh_token': refresh_token,
                    'grant_type': 'refresh_token',
                }
                revalidate_response = requests.post(
                    settings.TWITCH_TOKEN_URL, params=token_params
                )
                if revalidate_response.status_code != 200:
                    request.session.flush()
        except KeyError:
            request.session.flush()

        response = self.get_response(request)

        return response
