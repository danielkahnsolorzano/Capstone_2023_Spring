"""
This script tests if a connection can be established with the crazyflie. 

Adapted from:
https://www.bitcraze.io/documentation/repository/crazyflie-lib-python/master/user-guides/sbs_connect_log_param/
"""

"""
Before beggining:
In a terminal please write the following:
pip3 install cflib
"""

import logging
import time

import cflib.crtp
from cflib.crazyflie import Crazyflie
from cflib.crazyflie.syncCrazyflie import SyncCrazyflie
from cflib.utils import uri_helper

# URI to the Crazyflie to connect to
#uri = uri_helper.uri_from_env(default='radio://0/80/2M/E7E7E7E7E7')
uri = 'radio://0/80/2M/E7E7E7E7E7'
"""
check configuration with https://www.bitcraze.io/documentation/repository/crazyflie-clients-python/master/userguides/userguide_client/#firmware-configuration
"""


def simple_connect():
    print("Connection succesful.")
    time.sleep(3)
    print("Now disconnecting.")

if __name__ == '__main__':
    # Initialize the low-level drivers
    cflib.crtp.init_drivers()

    with SyncCrazyflie(uri, cf=Crazyflie(rw_cache='./cache')) as scf:

        simple_connect()
"""
The syncCrazyflie will create a synchronous Crazyflie instance with the specified link_uri.
"""







