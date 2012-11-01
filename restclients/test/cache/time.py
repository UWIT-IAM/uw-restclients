from django.test import TestCase
from django.conf import settings
from restclients.dao import SWS_DAO
from restclients.cache_implementation import TimeSimpleCache, FourHourCache
from restclients.models import CacheEntryTimed
from restclients.mock_http import MockHTTP
from datetime import timedelta
import re

class TimeCacheTest(TestCase):
    def test_simple_time(self):
        with self.settings(RESTCLIENTS_SWS_DAO_CLASS='restclients.dao_implementation.sws.File',
                            RESTCLIENTS_DAO_CACHE_CLASS='restclients.cache_implementation.TimeSimpleCache'):

            # Check initial state
            cache = TimeSimpleCache()
            response = cache.getCache('pws', '/student', {})
            self.assertEquals(response, None)
            response = cache.getCache('sws', '/student', {})
            self.assertEquals(response, None)
            sws = SWS_DAO()
            sws.getURL('/student', {})

            # Make sure there's a response there after the get
            hit = cache.getCache('sws', '/student', {})
            response = hit["response"]

            self.assertEquals(response.status, 200)

            html = response.data
            if not re.search('student/v4', html):
                self.fail("Doesn't contains a link to v4")


            # Make sure there's nothing for pws there after the get
            response = cache.getCache('pws', '/student', {})
            self.assertEquals(response, None)

    def test_4hour_time(self):
        with self.settings(RESTCLIENTS_SWS_DAO_CLASS='restclients.dao_implementation.sws.File',
                            RESTCLIENTS_DAO_CACHE_CLASS='restclients.cache_implementation.FourHourCache'):

            # Check initial state
            cache = TimeSimpleCache()
            response = cache.getCache('pws', '/student', {})
            self.assertEquals(response, None)
            response = cache.getCache('sws', '/student', {})
            self.assertEquals(response, None)
            sws = SWS_DAO()
            response = sws.getURL('/student', {})

            html = response.data
            if not re.search('student/v4', html):
                self.fail("Doesn't contains a link to v4")

            # Make sure there's a response there after the get
            hit = cache.getCache('sws', '/student', {})
            response = hit["response"]

            self.assertEquals(response.status, 200)

            html = response.data
            if not re.search('student/v4', html):
                self.fail("Doesn't contains a link to v4")


            # Make sure there's nothing for pws there after the get
            response = cache.getCache('pws', '/student', {})
            self.assertEquals(response, None)

    def test_errors(self):
        with self.settings(RESTCLIENTS_SWS_DAO_CLASS='restclients.dao_implementation.errors.Always500',
                            RESTCLIENTS_DAO_CACHE_CLASS='restclients.cache_implementation.FourHourCache'):

            cache = FourHourCache()
            response = cache.getCache('sws', '/invalid/url', {})
            self.assertEquals(response, None)

            sws = SWS_DAO()
            response = sws.getURL('/invalid/url', {})

            hit = cache.getCache('sws', '/invalid/url', {})
            response = hit["response"]

            self.assertEquals(response.status, 500)

            query = CacheEntryTimed.objects.filter(
                                                service="sws",
                                                url="/invalid/url",
                                              )


            # Make sure that invalid entry stops being returned after 5 mintes
            cache_entry = query[0]
            cache_entry.time_saved = cache_entry.time_saved - timedelta(minutes=5)
            cache_entry.save()

            hit = cache.getCache('sws', '/invalid/url', {})
            self.assertEquals(hit, None, "No hit on old, bad status codes")

            # Make sure bad responses don't overwrite good ones.
            ok_response = MockHTTP()
            ok_response.status = 200
            ok_response.data = "xx"

            cache.processResponse("test", "/ok/url", ok_response)

            cache_response = cache.getCache("test", "/ok/url", {})
            response = cache_response["response"]
            self.assertEquals(response.status, 200)


            bad_response = MockHTTP()
            bad_response.status = 500
            bad_response.data = "This is bad data"

            cache.processResponse("test", "/ok/url", bad_response)
            cache_response = cache.getCache("test", "/ok/url", {})
            response = cache_response["response"]
            self.assertEquals(response.status, 200)
            self.assertEquals(response.data, "xx")


            # Make sure that an old, good hit is returned when there's a fresh,
            # bad hit.
            ok_response = MockHTTP()
            ok_response.status = 200
            ok_response.data = "valid"

            cache.processResponse("sws", "/valid/url", ok_response)

            response = sws.getURL("/valid/url", {})
            self.assertEquals(response.status, 200)

            query = CacheEntryTimed.objects.filter(
                                                service="sws",
                                                url="/valid/url",
                                              )


            cache_entry = query[0]
            cache_entry.time_saved = cache_entry.time_saved - timedelta(hours=5)
            cache_entry.save()

            response = sws.getURL("/valid/url", {})
            self.assertEquals(response.status, 200)

            # But make sure eventually we stop using our cache.
            cache_entry.time_saved = cache_entry.time_saved - timedelta(hours=9)
            cache_entry.save()

            response = sws.getURL("/valid/url", {})
            self.assertEquals(response.status, 500)


