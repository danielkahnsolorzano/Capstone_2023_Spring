"""
This is an introduction script for Crazyflie control. 

Adapted from:
https://github.com/bitcraze/crazyflie-lib-python/blob/master/docs/user-guides/python_api.md
"""

"""
Before beggining:
In a terminal please write the following:
pip3 install cflib
"""

import cflib.crtp

cflib.crtp.init_drivers()
available = cflib.crtp.scan_interfaces()
for i in available:
    print "Interface with URI [%s] found and name/comment [%s]" % (i[0], i[1])
