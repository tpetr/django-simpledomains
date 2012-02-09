from django.conf import settings
from django.core.exceptions import MiddlewareNotUsed
import re

class DomainMiddleware(object):
    def __init__(self):
        urlconf_dict = getattr(settings, 'DOMAIN_URLCONF', None)

        # disable this middleware if no domain-specific urlconfs
        if not urlconf_dict:
            raise MiddlewareNotUsed

        # complie domain regexes
        try:
            self.urlconfs = {re.compile(k): v for k, v in urlconf_dict.items()}
        except TypeError:
            raise ImproperlyConfigured("settings.DOMAIN_URLCONF has invalid regex")

    def process_request(self, request):
        for regex, urlconf in self.urlconfs.items():
            m = regex.match(request.META.get('HTTP_HOST', ''))
            if not m: continue

            # found a match, set the urlconf and regex groups
            request.urlconf = urlconf
            request.domain_groupdict = m.groupdict()
            break
        return None
