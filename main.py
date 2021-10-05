import argparse
import math
from argparse import ArgumentParser

import numpy as np
from scipy.stats import rankdata

from atr_dict import AttrDict
from file_proc import read_data, write_file


def monotone_conjugation_check(input_path: str):
    xs, ys = read_data(input_path)
    N = len(xs)
    if N < 9:
        raise RuntimeError('For check we need more than 9 measures')

    rank_y = rankdata(ys, method="average")
    rank_y = -(rank_y - np.max(rank_y) - 1)
    p = int(round(N / 3))
    R1 = np.sum(rank_y[:p])
    R2 = np.sum(rank_y[-p:])
    error = (N + 0.5) * np.sqrt(p / 6)
    conj = (R1 - R2) / (p * (N - p))
    return math.ceil(R1 - R2), math.ceil(error), round(conj, 2)


def parse_args():
    parser = ArgumentParser(formatter_class=argparse.RawTextHelpFormatter)
    parser.add_argument("--input", "-i", type=str, default="./in.txt")
    parser.add_argument("--output", "-o", type=str, default="./out.txt")
    return parser.parse_args()


if __name__ == "__main__":
    args = AttrDict(vars(parse_args()))
    write_file(*monotone_conjugation_check(args.input), args.output)
