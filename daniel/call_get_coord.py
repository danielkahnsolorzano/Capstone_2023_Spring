from get_coord import ClientApp
import argparse

"""
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--server', help='Will autodiscover if not supplied')
    parser.add_argument('--rate', type=float, default=10, help='Rate at which to produce fake data (Hz)')
    parser.add_argument('--quiet', action='store_true')
    args = parser.parse_args()
    try:
        app = ClientApp.connect(args.server, args.rate, args.quiet)
        print(app.run())
    except natnet.DiscoveryError as e:
        print('Error:', e)
if __name__ == '__main__':
    main()
"""

"""
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
import natnet
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--server', help='Will autodiscover if not supplied')
    parser.add_argument('--rate', type=float, default=10, help='Rate at which to produce fake data (Hz)')
    parser.add_argument('--quiet', action='store_true')
    args = parser.parse_args()
    try:
        ClientApp.connect(args.server, args.rate, args.quiet)
        with open('data.txt', 'r') as data:
            coordinates = data.read().strip().split(',')
            x, y, z = float(coordinates[0]), float(coordinates[1]), float(coordinates[2])
            print(f"x:{x} y:{y} z:{z}")
        #data = open('data.txt')
        #pos = data.read()
        #print(pos)
    except natnet.DiscoveryError as e:
        print('Error:', e)
if __name__ == '__main__':
    main()
