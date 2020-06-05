import datetime

from django.conf import settings
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _
from rest_framework import exceptions
from rest_framework.authentication import TokenAuthentication
from .api_settings import TOKEN_EXPIRE


class ExpireTokenAuthentication(TokenAuthentication):
    def authenticate_credentials(self, key):
        model = self.get_model()
        try:
            token = model.objects.select_related('user').get(key=key)
        except model.DoesNotExist:
            raise exceptions.AuthenticationFailed(_('Token not exists.'))

        if not token.user.is_active:
            raise exceptions.AuthenticationFailed(_('User not active or deleted.'))

        if TOKEN_EXPIRE:
            assert type(TOKEN_EXPIRE) == int, "TOKEN_EXPIRE type must be Int"
            if timezone.now() > token.created + datetime.timedelta(days=int(TOKEN_EXPIRE)):
                raise exceptions.AuthenticationFailed(_('Token has expired'))

        return (token.user, token)
