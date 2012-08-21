from django.utils.importlib import import_module
from django.conf import settings
from django.core.exceptions import *

class DAO(object):
    def __new__(*args, **named_args):
        if hasattr(settings, 'RESTCLIENTS_DAO_CLASS'):
            # This is all taken from django's static file finder
            module, attr = settings.RESTCLIENTS_DAO_CLASS.rsplit('.', 1)
            try:
                mod = import_module(module)
            except ImportError, e:
                raise ImproperlyConfigured('Error importing module %s: "%s"' %
                                           (module, e))
            try:
                DAOModule = getattr(mod, attr)
            except AttributeError:
                raise ImproperlyConfigured('Module "%s" does not define a "%s" '
                                   'class.' % (module, attr))

            return DAOModule()
        else:
            raise ImproperlyConfigured("Don't have a default DAO object yet :(")
