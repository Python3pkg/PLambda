#!/usr/bin/env python


import sys

from actor import Actor

from src.drones.simple_drone import SimpleDrone

usage = """
Usage: {0} <actor name>
"""


def main(cmd):
    if len(cmd) != 2:
        print usage.format(cmd[0])
        return 1
    drone = SimpleDrone("droneZero")
    Actor(cmd[1], drone).begin()

    
if __name__ == '__main__':
    sys.exit(main(sys.argv))
