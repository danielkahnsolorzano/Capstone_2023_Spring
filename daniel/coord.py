"""
Tryign something different.
"""

import pynatnet

def callback(timestamp, rigid_bodies, markers, force_plates):
    for body in rigid_bodies:
        if body.id == 60:
            position = body.position
            print(f"Position: ({position[0]}, {position[1]}, {position[2]})")

client = pynatnet.connect()
client.set_callback(callback)

while True:
    client.poll()
