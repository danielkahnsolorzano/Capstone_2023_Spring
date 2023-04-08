"""
get back drone position
"""

from __future__ import print_function
from typing import List, Tuple
import time
import attr
import natnet

@attr.s
class ClientApp(object):
    _client = attr.ib()
    _quiet = attr.ib()
    _last_printed = attr.ib(0)

    @classmethod
    def connect(cls, server_name, rate, quiet):
        if server_name == 'fake':
            client = natnet.fakes.SingleFrameFakeClient.fake_connect(rate=rate)
        else:
            client = natnet.Client.connect(server_name)
        if client is None:
            return None
        return cls(client, quiet)

    def run(self):
        if self._quiet:
            self._client.set_callback(self.callback_quiet)
        else:
            self._client.set_callback(self.callback)
        #self._client.spin()

    def callback(self, rigid_bodies, markers, timing):
        """
        :type rigid_bodies: list[RigidBody]
        :type markers: list[LabelledMarker]
        :type timing: TimestampAndLatency
        """
        print()
        print('{:.1f}s+: Received mocap frame'.format(timing.timestamp))
        if rigid_bodies:
            drone = rigid_bodies[0] # accesed first, but we need to find which one is our drone
            dronePos = drone.position
        """
        if markers:
            droneMarkers = markers[0] # accesed first, but we need to find which one is our drone
            droneMarkersPos = droneMarkers.position
        """

    def callback_quiet(self, *_):
        if time.time() - self._last_printed > 1:
            print('.')
            self._last_printed = time.time()

#FIXME

def get_drone_pos(server_name: str, rate: float, quiet: bool) -> List[float]:
    try:
        app = ClientApp.connect('fake' if args.fake else server_name, rate, quiet)
        app.run()
        if app.dronePos is not None:
            return app.dronePos
    except natnet.DiscoveryError as e:
        print('Error:', e)
    return []


"""
# Use:

from dan0330 import get_drone_pos

# Call the function with the server name, rate, and quiet flag
pos = get_drone_pos('myserver', 10.0, False)

# Use the position of the drone
if len(pos) == 3:
    print('Drone position:', pos)
else:
    print('Error: could not get drone position')
"""