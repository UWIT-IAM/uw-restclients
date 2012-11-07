from django.utils.importlib import import_module
from django.conf import settings
from django.core.exceptions import *
from restclients.dao_implementation.pws import File as PWSFile
from restclients.dao_implementation.sws import File as SWSFile
from restclients.dao_implementation.gws import File as GWSFile
from restclients.dao_implementation.book import File as BookFile
from restclients.dao_implementation.canvas import File as CanvasFile
from restclients.dao_implementation.nws import File as NWSFile
from restclients.dao_implementation.sms import Local as SMSLocal
from restclients.dao_implementation.amazon_sqs import Local as SQSLocal
from restclients.cache_implementation import NoCache

class DAO_BASE(object):
    def _getModule(self, settings_key, default_class):
        if hasattr(settings, settings_key):
            # This is all taken from django's static file finder
            module, attr = getattr(settings, settings_key).rsplit('.', 1)
            try:
                mod = import_module(module)
            except ImportError, e:
                raise ImproperlyConfigured('Error importing module %s: "%s"' %
                                           (module, e))
            try:
                config_module = getattr(mod, attr)
            except AttributeError:
                raise ImproperlyConfigured('Module "%s" does not define a '
                                   '"%s" class' % (module, attr))
            return config_module()
        else:
            return default_class()

class MY_DAO(DAO_BASE):
    def _getCache(self):
        return self._getModule('RESTCLIENTS_DAO_CACHE_CLASS', NoCache)

    def _getURL(self, service, url, headers):
        dao = self._getDAO()
        cache = self._getCache()
        cache_response = cache.getCache(service, url, headers)
        if cache_response != None:
            if "response" in cache_response:
                return cache_response["response"]
            if "headers" in cache_response:
                headers = cache_response["headers"]

        response = dao.getURL(url, headers)

        cache_post_response = cache.processResponse(service, url, response)

        if cache_post_response != None:
            if "response" in cache_post_response:
                return cache_post_response["response"]

        return response


class SWS_DAO(MY_DAO):
    def getURL(self, url, headers):
        return self._getURL('sws', url, headers)

    def _getDAO(self):
        return self._getModule('RESTCLIENTS_SWS_DAO_CLASS', SWSFile)


class PWS_DAO(MY_DAO):
    def getURL(self, url, headers):
        return self._getURL('pws', url, headers)

    def _getDAO(self):
        return self._getModule('RESTCLIENTS_PWS_DAO_CLASS', PWSFile)


class GWS_DAO(MY_DAO):
    def getURL(self, url, headers):
        return self._getURL('gws', url, headers)

    def _getDAO(self):
        return self._getModule('RESTCLIENTS_GWS_DAO_CLASS', GWSFile)


class Book_DAO(MY_DAO):
    def getURL(self, url, headers):
        return self._getURL('books', url, headers)

    def _getDAO(self):
        return self._getModule('RESTCLIENTS_BOOK_DAO_CLASS', BookFile)


class Canvas_DAO(MY_DAO):
    def getURL(self, url, headers):
        return self._getURL('canvas', url, headers)

    def _getDAO(self):
        return self._getModule('RESTCLIENTS_CANVAS_DAO_CLASS', CanvasFile)


class AmazonSQS_DAO(MY_DAO):
    def create_queue(self, queue_name):
        dao = self._getDAO()
        return dao.create_queue(queue_name)

    def get_queue(self, queue_name):
        dao = self._getDAO()
        res = dao.get_queue(queue_name)
        return res

    def _getDAO(self):
        return self._getModule('AMAZON_SQS_DAO_CLASS', SQSLocal)


class SMS_DAO(MY_DAO):
    def create_message(self, to, body):
        dao = self._getDAO()
        return dao.create_message(to, body)

    def send_message(self, message):
        dao = self._getDAO()
        return dao.send_message(message)

    def _getDAO(self):
        return self._getModule('SMS_DAO_CLASS', SMSLocal)


class NWS_DAO(MY_DAO):
    def getURL(self, url, headers):
        return self._getURL('nws', url, headers)

    def _getDAO(self):
        return self._getModule('RESTCLIENTS_NWS_DAO_CLASS', NWSFile)
