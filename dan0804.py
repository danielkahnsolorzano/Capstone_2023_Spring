# coding: utf-8
"""
NatNet client https://github.com/mje-nz/python_natnet/blob/master/LICENSE
"""

from __future__ import print_function
import argparse
import time
import attr
import natnet

@attr.s
class ClientApp(object):
    _client = attr.ib()
    _quiet = attr.ib()
    _last_printed = attr.ib(0)
    retPos = attr.ib(default=None)
    @classmethod
    def connect(cls, server_name, rate, quiet):
        client = natnet.Client.connect(server_name)
        if client is None:
            return None
        return cls(client, quiet)
    def run(self):
        self._client.set_callback(self.callback)
        self._client.spin() # spin(timeout=None) Continuously receive and process messages
        """
        if self.retPos is not None:
            print("RETURNING POSITION")
            return self.retPos
        else:
            print(self.retPos)
            print("TRYING AGAIN")
            self.run()
        """
    def callback(self, rigid_bodies, markers, timing):
        if rigid_bodies:
            for body in rigid_bodies: 
                if body.id_==60:
                    bodyPos = body.position
                    #print(bodyPos)
                    self.retPos = bodyPos
                    print(self.retPos)
                    print(f'x:{bodyPos[0]} y:{bodyPos[1]} z:{bodyPos[2]}')

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--server', help='Will autodiscover if not supplied')
    parser.add_argument('--rate', type=float, default=10, help='Rate at which to produce fake data (Hz)')
    parser.add_argument('--quiet', action='store_true')
    args = parser.parse_args()
    try:
        app = ClientApp.connect(args.server, args.rate, args.quiet)
        app.run()
        """
        currPos = app.run()
        print("GOT HERE")
        print(currPos)
        """
    except natnet.DiscoveryError as e:
        print('Error:', e)

if __name__ == '__main__':
    main()
