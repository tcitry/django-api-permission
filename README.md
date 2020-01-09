# Django-API-Permission

![](https://img.shields.io/pypi/v/django-api-permission.svg?label=django-api-permission)

## Intro

A Django api permission manager that helps you custom api url in regular expression and control access

## Quick Start

### Install

```
pip install django-api-permission
```

### add to INSTALLED_APPS and MIDDLEWARE

```
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

## Demo

![](./demo1.png)

![](./demo2.png)

![](./demo3.png)
