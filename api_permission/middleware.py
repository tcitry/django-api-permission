from django.contrib.auth.models import AnonymousUser
from django.http.response import JsonResponse
from django.utils.deprecation import MiddlewareMixin
from rest_framework.authtoken.models import Token
from rest_framework import status
from .exceptions import APIPermissionException
from .models import APIPermissionModel
from .api_settings import API_PREFIX, PERMISSION_DENIED_CODE, AUTHORIZATION_HEADER, ADMIN_SITE_PATH
import logging
import re


class APIPermCheckMiddleware(MiddlewareMixin):

    def process_request(self, request):
        path = request.path
        method = request.method
        header_token = request.META.get(AUTHORIZATION_HEADER, None)
        user = request.user or AnonymousUser()
        if header_token:
            try:
                token = header_token.strip().split(' ')
                assert len(token) > 0, f"token maybe invalid: {header_token}"
                token_obj = Token.objects.get(key=token[-1])
                user = token_obj.user
            except Token.DoesNotExist as e:
                msg = f"api_permission checker: token not exists: {e}"
                return self._return_403_res(msg)
            except Exception as e:
                msg = f"{e}"
                raise APIPermissionException(msg)

        api_prefix_list = []
        if type(API_PREFIX) == str:
            if API_PREFIX == '/':
                api_prefix_list = ['/']
            else:
                if not API_PREFIX.startswith('/'):
                    api_prefix_list.append('/' + str(API_PREFIX))
                else:
                    api_prefix_list = API_PREFIX
        elif type(API_PREFIX) == list:
            for prefix in API_PREFIX:
                if not prefix.startswith('/'):
                    prefix = '/' + str(prefix)
                api_prefix_list.append(prefix)

        if not path.startswith(ADMIN_SITE_PATH) and not user.is_superuser:
            for api_prefix in api_prefix_list:
                if path.startswith(api_prefix):
                    if not self._has_permission(path, user, method):
                        return self._return_403_res(f'permission denied: user: {user}, method: {method}, path: {path}')

    def _has_permission(self, path, user, method):
        groups = user.groups.all()
        queryset = APIPermissionModel.objects.filter(group__in=groups, method__in=[method, APIPermissionModel.ALL], active=True)
        for api in queryset:
            if re.match(api.pattern, path):
                if api.method in [APIPermissionModel.ALL, method]:
                    return True
        return False

    def _return_403_res(self, msg):
        res = {
            'code': PERMISSION_DENIED_CODE,
            'msg': msg,
        }
        return JsonResponse(res, status=status.HTTP_403_FORBIDDEN)
