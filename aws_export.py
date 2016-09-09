

from __future__ import generators, print_function, division

import PyViability as viab

import numpy as np


import sys, os
import argparse
import pickle

SPACING = " "*4

def recursive_dict2string(dic, prefix=""):
    ret = ""
    for key in sorted(dic):
        assert isinstance(key, str)
        ret += prefix + key + " = "
        if isinstance(dic[key], dict):
            ret += "{\n"
            ret += recursive_dict2string(dic[key], prefix=prefix+SPACING)
            ret += "}\n"
        else:
            ret += repr(dic[key]) + "\n"
    return ret



if __name__=="__main__":
    parser = argparse.ArgumentParser(
        description="Export an AWS - TSM file to text.",
    )
    parser.add_argument("input_file", metavar="input-file",
                        help="file with the tsm data")
    parser.add_argument("txt_file", metavar="txt-file",
                        help="output text file")
    parser.add_argument("-f", "--force", action="store_true",
                        help="overwrite text file if already existing")

    args = parser.parse_args()

    if not args.force:
        if os.path.isfile(args.txt_file):
            parser.error("'{}' exists already, use '--force' option to overwrite".format(args.txt_file))

    if args.txt_file == args.input_file:
        parser.error("'txt-file' and 'output-file' should be different from each other, not both '{}'".format(args.input_file))

    with open(args.input_file, "rb") as f:
        header, data = pickle.load(f)

    header_txt = "#"*80 + "\n"
    header_txt += recursive_dict2string(header)
    header_txt += "#"*80 + "\n"

    for region in viab.REGIONS:
        header_txt += "{} = {:>2d}\n".format(region, getattr(viab, region))
    header_txt += "#"*80

    states = data["states"]

    print(header_txt)

    print("saving to {!r} ... ".format(args.txt_file), end="", flush=True)
    np.savetxt(args.txt_file, states, fmt="%3i", header=header_txt, comments="")
    print("done")
