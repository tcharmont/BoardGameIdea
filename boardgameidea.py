import data

import argparse
import random


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-m", type=int, help="define the mechanics number")
    parser.add_argument("-v", "--verbose", action="store_true", help="increase the verbosity")
    args = parser.parse_args()
    print("### Category ###")
    print(data.categories[random.randrange(len(data.categories))] + "\n")
    mechanics = draw_mechanics(args.m)
    print("### Mechanics ###")
    for mechanic in mechanics:
        print(mechanic + " : " + data.mechanics.get(mechanic))


def draw_mechanics(nb):
    return random.sample(list(data.mechanics.keys()), nb)


if __name__ == "__main__":
    main()
