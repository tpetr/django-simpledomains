====================
django-simpledomains
====================

An easy way to support multiple domains in your Django app.

Getting Started
===============

- Add simpledomains to your PYTHONPATH

- Add simpledomains.middleware.DomainMiddleware to the MIDDLEWARE_CLASSES list in settings.py:

::

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    ...
    'simpledomains.middleware.DomainMiddleware',
)

- Create a domain --> urlconf mapping dict named DOMAIN_URLCONFS in settings.py:

::

DOMAIN_URLCONFS = {
    r'test.domain.com': 'myapp.urls',
    r'(?P<user>\w+).domain.com': 'myall.urls_userpage',
}


**Note**: Requests that match nothing will default to the ROOT_URLCONF setting. If you specify capture groups in your domain regex, they'll be accessible via request.domain_groupdict
