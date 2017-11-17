import connexion
from swagger_server.models.door_command import DoorCommand
from swagger_server.models.door_state import DoorState
from swagger_server.models.error_state import ErrorState
from datetime import date, datetime
from typing import List, Dict
from six import iteritems
from ..util import deserialize_date, deserialize_datetime


def get_door():
    """
    Returns the current state of the door
    Returns the current state of the door.  One of OPEN, CLOSED, OPENING, or CLOSING

    :rtype: DoorState
    """
    return 'do some magic!'


def post_door(body):
    """
    Controls the garage door
    Sends the garage door OPEN and CLOSE commands
    :param body: Command to send to the garage door
    :type body: dict | bytes

    :rtype: DoorState
    """
    if connexion.request.is_json:
        body = DoorCommand.from_dict(connexion.request.get_json())
    return 'do some magic!'
