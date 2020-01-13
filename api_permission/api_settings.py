from django.conf import settings


API_PREFIX = getattr(settings, 'API_PREFIX', '/api/')
