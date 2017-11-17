import connexion
from swagger_server.models.error_state import ErrorState
from swagger_server.models.light_state import LightState
from datetime import date, datetime
from typing import List, Dict
from six import iteritems
from ..util import deserialize_date, deserialize_datetime


def get_light():
    """
    Returns the current light level
    Returns the current illumination level in the garage in Lux

    :rtype: LightState
    """
    return 'do some magic!'


def light_post():
    """
    Controls the garage light
    Toggle the garage light in state

    :rtype: LightState
    """
    return 'do some magic!'
