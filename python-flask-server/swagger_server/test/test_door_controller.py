# coding: utf-8

from __future__ import absolute_import

from swagger_server.models.door_command import DoorCommand
from swagger_server.models.door_state import DoorState
from swagger_server.models.error_state import ErrorState
from . import BaseTestCase
from six import BytesIO
from flask import json


class TestDoorController(BaseTestCase):
    """ DoorController integration test stubs """

    def test_get_door(self):
        """
        Test case for get_door

        Returns the current state of the door
        """
        response = self.client.open('/v1/door',
                                    method='GET',
                                    content_type='application/json')
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_post_door(self):
        """
        Test case for post_door

        Controls the garage door
        """
        body = DoorCommand()
        response = self.client.open('/v1/door',
                                    method='POST',
                                    data=json.dumps(body),
                                    content_type='application/json')
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
