
import subprocess as sp
import argparse


if __name__ == "__main__":
    a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    for argv in a[1:-1]:
        print("{argv:<4}{argv:<20}{argv:<4}".format(argv=str(argv)))