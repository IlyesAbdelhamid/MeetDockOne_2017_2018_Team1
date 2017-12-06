import sys
sys.path.insert(0, "./lib/")

import pdb2grid
import pdb_resdepth
import fft
import electrostatic
import argparse

def get_args():
    '''This function parses and return arguments passed in'''
    parser = argparse.ArgumentParser(
        prog='MeetDockOne',
        description='MeetDockOne scores a protein complex docking',
        version=0.9)
    parser.add_argument('file', help=".pdb complex file")
    parser.add_argument(
        '-shape',
        action="store_true",
        help="compute shape complementarity")
    parser.add_argument(
        '-electro',
        action="store_true",
        help="compute Electrostatic interactions")

    parser.add_argument(
        '-jones',
        action="store_true",
        help="compute Lennard-Jones interactions")

    parser.add_argument(
        '-proba',
        action="store_true",
        help="Compute knowledge based interactions")

    parser.add_argument(
        '-foldx',
        action="store_true",
        help="Scores with FoldX")

    parser.add_argument(
        '-pH',
        default=7,
        type=int,
        help="pH for electrostatic interactions. Default = 7")

    parser.add_argument(
        '-depth',
        default=4,
        type=float,
        help="Threshold for surface residue determination (Angstrom). Default = 4")

    parser.add_argument(
        '-dist',
        default=8.5,
        type=float,
        help="Threshold for interface determination (Angstrom). Default = 8.5")
    args = parser.parse_args()

    myfile = args.file
    shape = shape
    electro = args.electro
    jones = args.jones
    proba = args.proba
    foldx = args.foldx
    pH = args.pH
    depth = args.depth
    dist = args.dist



    return(myfile, shape, electro, jones, proba, foldx, pH, depth, dist)

if __name__ == "__main__":
     # do something
     pass
