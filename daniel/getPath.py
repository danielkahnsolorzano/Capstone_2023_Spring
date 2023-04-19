import argparse
import attr
import natnet
import sys
import numpy as np
import time

@attr.s
class ClientApp(object):
    _client = attr.ib()
    _quiet = attr.ib()
    @classmethod
    def connect(cls, server_name, rate, quiet):
        client = natnet.Client.connect(server_name)
        if client is None:
            return None
        app = cls(client, quiet)
        app.run()
    def run(self):
        self._client.set_callback(self.callback)
        self._client.spin() # spin(timeout=None) Continuously receive and process messages
    def callback(self, rigid_bodies, markers, timing):
        if rigid_bodies:
            for body in rigid_bodies: 
                if body.id_==60:
                    bodyPos = body.position
                    print(bodyPos)
                    if bodyPos is not None:
                        with open('data.txt', 'a') as dataFile:
                          np.savetxt(dataFile, np.array(bodyPos))

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--server', help='Will autodiscover if not supplied')
    parser.add_argument('--rate', type=float, default=10, help='Rate at which to produce fake data (Hz)')
    parser.add_argument('--quiet', action='store_true')
    args = parser.parse_args()
    try:
        ClientApp.connect(args.server, args.rate, args.quiet)
    except natnet.DiscoveryError as e:
        print('Error:', e)
if __name__ == '__main__':
    main()
