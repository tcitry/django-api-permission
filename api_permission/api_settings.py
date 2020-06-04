from django.conf import settings

API_PERMISSION_CONF = getattr(settings, "API_PERMISSION_CONF", {})

API_PREFIX = API_PERMISSION_CONF.get('API_PREFIX', ['/api/'])
PERMISSION_DENIED_CODE = API_PERMISSION_CONF.get('PERMISSION_DENIED_CODE', 1)
AUTHORIZATION_HEADER = API_PERMISSION_CONF.get('AUTHORIZATION_HEADER', 'HTTP_AUTHORIZATION')
ADMIN_SITE_PATH = API_PERMISSION_CONF.get('ADMIN_SITE_PATH', '/admin/')
