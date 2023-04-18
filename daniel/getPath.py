from get_coord import ClientApp
import argparse
import attr
import natnet
import sys
import numpy as np

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
        self._client.spin(timeout=5) # spin(timeout=None) Continuously receive and process messages
    def callback(self, rigid_bodies, markers, timing):
        if rigid_bodies:
            for body in rigid_bodies: 
                if body.id_==60:
                    bodyPos = body.position
                    if bodyPos is not None:
                        with open('data.txt', 'a') as f:
                          np.savetxt(f, np.array(bodyPos)[None], header=None)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--server', help='Will autodiscover if not supplied')
    parser.add_argument('--rate', type=float, default=10, help='Rate at which to produce fake data (Hz)')
    parser.add_argument('--quiet', action='store_true')
    args = parser.parse_args()
    try:
        ClientApp.connect(args.server, args.rate, args.quiet)
        with open('data.txt', 'r') as data:
            coordinates = data.read().strip().split('\n')
            x, y, z = float(coordinates[0]), float(coordinates[1]), float(coordinates[2])
            print(f"x:{x} y:{y} z:{z}")
    except natnet.DiscoveryError as e:
        print('Error:', e)
if __name__ == '__main__':
    main()
