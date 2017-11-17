# coding: utf-8

from __future__ import absolute_import

from swagger_server.models.error_state import ErrorState
from swagger_server.models.light_state import LightState
from . import BaseTestCase
from six import BytesIO
from flask import json


class TestLightController(BaseTestCase):
    """ LightController integration test stubs """

    def test_get_light(self):
        """
        Test case for get_light

        Returns the current light level
        """
        response = self.client.open('/v1/light',
                                    method='GET',
                                    content_type='application/json')
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_light_post(self):
        """
        Test case for light_post

        Controls the garage light
        """
        response = self.client.open('/v1/light',
                                    method='POST',
                                    content_type='application/json')
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
