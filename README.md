# Django-API-Permission

![](https://img.shields.io/pypi/v/django-api-permission.svg?label=django-api-permission)

## 1. Intro

A Django api permission manager that helps you custom api url in regular expression and control access.

## 2. Quick Start

### 2.1 Install

```
pip install django-api-permission
```

### 2.2 add to INSTALLED_APPS and MIDDLEWARE

```python
INSTALLED_APPS = [
    ...
    'api_permission',
    ...
]

MIDDLEWARE = [
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    ...
    'api_permission.middleware.APIPermCheckMiddleware',
]
```

### 2.3 migrate

```
./manage.py migrate api_permission
```

### 2.4 settings

set `API_PERMISSION_CONF` in your settings.py as a dict.

```python
API_PERMISSION_CONF = {
    'API_PREFIX': ['api/topic/'], # default is /
    'PERMISSION_DENIED_CODE': 1, # default is 1
    'AUTHORIZATION_HEADER': 'HTTP_AUTHORIZATION', # default is HTTP_AUTHORIZATION
    'ADMIN_SITE_PATH': '/admin/', # default is /admin/
    'TOKEN_EXPIRE': 15, # unit is days, default is None, which won't check token expire.
}
```

You can custom `API_PREFIX` as a str like `'/'` or list like `['api/account', 'api/topic']`.

**When you set `TOKEN_EXPIRE`, you need add below in your `REST_FRAMEWORK` settings.**

```python
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        ...
        'api_permission.authentication.ExpireTokenAuthentication',
    ),
}
```

## 3. Demo

### 3.1 list

![](./demo/demo1.png)

### 3.2 edit

![](./demo/demo2.png)

### 3.3 result

![](./demo/demo3.png)
