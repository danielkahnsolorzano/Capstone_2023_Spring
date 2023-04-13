# coding: utf-8
"""
NatNet client https://github.com/mje-nz/python_natnet/blob/master/LICENSE
"""

import argparse
import attr
import natnet

"""
@attr.s
class ClientApp(object):
    _client = attr.ib()
    _quiet = attr.ib()
    @classmethod
    def connect(cls, server_name, rate, quiet):
        client = natnet.Client.connect(server_name)
        if client is None:
            return None
        return cls(client, quiet)
    def run(self):
        self._client.set_callback(self.callback)
        self._client.spin() # spin(timeout=None) Continuously receive and process messages
    def callback(self, rigid_bodies, markers, timing):
        if rigid_bodies:
            for body in rigid_bodies: 
                if body.id_==60:
                    bodyPos = body.position
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
    except natnet.DiscoveryError as e:
        print('Error:', e)
if __name__ == '__main__':
    main()
"""

"""
@attr.s
class ClientApp(object):
    _client = attr.ib()
    _quiet = attr.ib()
    _retPos = attr.ib(default=None)
    @classmethod
    def connect(cls, server_name, rate, quiet):
        client = natnet.Client.connect(server_name)
        if client is None:
            return None
        return cls(client, quiet)
    def run(self):
        self._client.set_callback(self.callback)
        if self._retPos is not None:
            print("RETURNING POSITION") #DEBUGGING
            print(self._retPos) #DEBUGGING
            return self._retPos
        else:
            print("TRYING AGAIN") #DEBUGGING
            print(self._retPos) #DEBUGGING
            self.run()
    def callback(self, rigid_bodies, markers, timing):
        if rigid_bodies:
            for body in rigid_bodies: 
                if body.id_==60:
                    bodyPos = body.position
                    self._retPos = bodyPos
                    print(self._retPos) #DEBUGGING
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--server', help='Will autodiscover if not supplied')
    parser.add_argument('--rate', type=float, default=10, help='Rate at which to produce fake data (Hz)')
    parser.add_argument('--quiet', action='store_true')
    args = parser.parse_args()
    try:
        app = ClientApp.connect(args.server, args.rate, args.quiet)
        currPos = app.run()
        print("GOT HERE") #DEBUGGING
        print(currPos) #DEBUGGING
    except natnet.DiscoveryError as e:
        print('Error:', e)
if __name__ == '__main__':
    main()
"""

"""
@attr.s
class ClientApp(object):
    _client = attr.ib()
    _quiet = attr.ib()
    _retPos = attr.ib(default=None)
    @classmethod
    def connect(cls, server_name, rate, quiet):
        client = natnet.Client.connect(server_name)
        if client is None:
            return None
        return cls(client, quiet)
    def run(self):
        if self.__class__._retPos is not None:
            print("RETURNING POSITION") #DEBUGGING
            print(self.__class__._retPos) #DEBUGGING
            return self.__class__._retPos
        else:
            print("TRYING AGAIN") #DEBUGGING
            print(self.__class__._retPos) #DEBUGGING
            self.run()
    def callback(self, rigid_bodies, markers, timing):
        if rigid_bodies:
            for body in rigid_bodies: 
                if body.id_==60:
                    bodyPos = body.position
                    self.__class__._retPos = bodyPos #MAYBE THIS WILL WORK
                    print(self.__class__._retPos) #DEBUGGING
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--server', help='Will autodiscover if not supplied')
    parser.add_argument('--rate', type=float, default=10, help='Rate at which to produce fake data (Hz)')
    parser.add_argument('--quiet', action='store_true')
    args = parser.parse_args()
    try:
        app = ClientApp.connect(args.server, args.rate, args.quiet)
        currPos = app.run()
        print("GOT HERE") #DEBUGGING
        print(currPos) #DEBUGGING
    except natnet.DiscoveryError as e:
        print('Error:', e)
if __name__ == '__main__':
    main()
"""

"""
@attr.s
class ClientApp(object):
    _client = attr.ib()
    _quiet = attr.ib()
    _retPos = attr.ib(default=None)
    @classmethod
    def connect(cls, server_name, rate, quiet):
        client = natnet.Client.connect(server_name)
        if client is None:
            return None
        app = cls(client, quiet)
        app.run
        while app._retPos is None:
            print("TRYING AGAIN") #DEBUGGING
            app.run()
        print("RETURNING POSITION") #DEBUGGING
        print(app._retPos) #DEBUGGING
        return app._retPos
    def run(self):
        self._client.set_callback(self.callback)
    def callback(self, rigid_bodies, markers, timing):
        if rigid_bodies:
            for body in rigid_bodies: 
                if body.id_==60:
                    bodyPos = body.position
                    self._retPos = bodyPos
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--server', help='Will autodiscover if not supplied')
    parser.add_argument('--rate', type=float, default=10, help='Rate at which to produce fake data (Hz)')
    parser.add_argument('--quiet', action='store_true')
    args = parser.parse_args()
    try:
        pos = ClientApp.connect(args.server, args.rate, args.quiet)
        print(pos)
    except natnet.DiscoveryError as e:
        print('Error:', e)
if __name__ == '__main__':
    main()
"""

"""
import sys
@attr.s
class ClientApp(object):
    _client = attr.ib()
    _quiet = attr.ib()
    @classmethod
    def connect(cls, server_name, rate, quiet):
        client = natnet.Client.connect(server_name)
        if client is None:
            return None
        return cls(client, quiet)
    def run(self):
        self._client.set_callback(self.callback)
        self._client.spin() # spin(timeout=None) Continuously receive and process messages
    def callback(self, rigid_bodies, markers, timing):
        if rigid_bodies:
            for body in rigid_bodies: 
                if body.id_==60:
                    bodyPos = body.position
                    if bodyPos is not None:
                        sys.exit(bodyPos)                 
# def main():
#     parser = argparse.ArgumentParser()
#     parser.add_argument('--server', help='Will autodiscover if not supplied')
#     parser.add_argument('--rate', type=float, default=10, help='Rate at which to produce fake data (Hz)')
#     parser.add_argument('--quiet', action='store_true')
#     args = parser.parse_args()
#     try:
#         app = ClientApp.connect(args.server, args.rate, args.quiet)
#         app.run()
#     except natnet.DiscoveryError as e:
#         print('Error:', e)
# if __name__ == '__main__':
#     main()
"""

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
        self._client.spin() # spin(timeout=None) Continuously receive and process messages
    def callback(self, rigid_bodies, markers, timing):
        if rigid_bodies:
            for body in rigid_bodies: 
                if body.id_==60:
                    bodyPos = body.position
                    if bodyPos is not None:
                        np.savetxt('data.txt', np.array(bodyPos))
                        sys.exit() 
