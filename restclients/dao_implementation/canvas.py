"""
Contains Instructure Canvas DAO implementations.
"""

from restclients.dao_implementation.live import get_con_pool, get_live_url
from restclients.dao_implementation.mock import get_mockdata_url, post_mockdata_url
from restclients.dao_implementation.mock import delete_mockdata_url, put_mockdata_url
from django.conf import settings
from os.path import abspath, dirname


class File(object):
    """
    The File DAO implementation returns generally static content.  Use this
    DAO with this configuration:

    RESTCLIENTS_CANVAS_DAO_CLASS = 'restclients.dao_implementation.canvas.File'
    """
    def getURL(self, url, headers):
        return get_mockdata_url("canvas", "file", url, headers)

    def putURL(self, url, headers, body):
        response = put_mockdata_url("canvas", "file", url, headers, body)
        if response.status == 400:
            return response

        path = abspath(dirname(__file__) + "/../resources/canvas/file" +
                       url + ".PUT")

        try:
            handle = open(path)
            response.data = handle.read()
            response.status = 200
        except IOError:
            response.status = 404

        return response

    def postURL(self, url, headers, body):
        response = post_mockdata_url("canvas", "file", url, headers, body)
        if response.status == 400:
            return response

        path = abspath(dirname(__file__) + "/../resources/canvas/file" +
                       url + ".POST")
        try:
            handle = open(path)
            response.data = handle.read()
            response.status = 200
        except IOError:
            response.status = 404

        return response

    def deleteURL(self, url, headers):
        return delete_mockdata_url("canvas", "file", url, headers)


class Live(object):
    """
    This DAO provides real data.  It requires the following configuration:

    RESTCLIENTS_CANVAS_HOST="https://canvas.uw.edu"
    RESTCLIENTS_CANVAS_OAUTH_BEARER="..."
    """
    pool = None

    def getURL(self, url, headers):
        host = settings.RESTCLIENTS_CANVAS_HOST
        bearer_key = settings.RESTCLIENTS_CANVAS_OAUTH_BEARER

        headers["Authorization"] = "Bearer %s" % bearer_key

        if Live.pool == None:
            Live.pool = get_con_pool(host, None, None)
        return get_live_url(Live.pool, 'GET',
                            host, url, headers=headers)

    def putURL(self, url, headers, body):
        host = settings.RESTCLIENTS_CANVAS_HOST
        bearer_key = settings.RESTCLIENTS_CANVAS_OAUTH_BEARER

        headers["Authorization"] = "Bearer %s" % bearer_key

        if Live.pool == None:
            Live.pool = get_con_pool(host, None, None)
        return get_live_url(Live.pool, 'PUT',
                            host, url, headers=headers, body=body)

    def postURL(self, url, headers, body):
        host = settings.RESTCLIENTS_CANVAS_HOST
        bearer_key = settings.RESTCLIENTS_CANVAS_OAUTH_BEARER

        headers["Authorization"] = "Bearer %s" % bearer_key

        if Live.pool == None:
            Live.pool = get_con_pool(host, None, None)
        return get_live_url(Live.pool, 'POST',
                            host, url, headers=headers, body=body)

    def deleteURL(self, url, headers):
        host = settings.RESTCLIENTS_CANVAS_HOST
        bearer_key = settings.RESTCLIENTS_CANVAS_OAUTH_BEARER

        headers["Authorization"] = "Bearer %s" % bearer_key

        if Live.pool == None:
            Live.pool = get_con_pool(host, None, None)
        return get_live_url(Live.pool, 'DELETE',
                            host, url, headers=headers)
