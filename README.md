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

### 2.3 migrate

```
./manage.py migrate api_permission
```

## 3. Demo

### 3.1 list

![](./demo1.png)

### 3.2 edit

![](./demo2.png)

### 3.3 result

![](./demo3.png)
