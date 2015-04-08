__author__ = 'Sebastian Schüpbach'

import argparse
import random

parser = argparse.ArgumentParser(description="Generate a random string")
parser.add_argument('length', metavar='<int>', type=int, help='Length of string')
args = parser.parse_args()

chars = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'ä', 'ö', 'ü']
chars.extend([x.upper() for x in chars])
chars.extend(['§', '°', '+', '"', '*', '%', '&', '/', '(', ')', '=', '|', '@', '#', '¬', '¢', '?', '!', ']', '[', '{',
                '}', '-', '_', '$', '£', '.', ',', ':', ';', '<', '>', '€', '¼', '½'])
chars.extend([x for x in range(0,10)])

for x in range(args.length):
    random.seed()
    i = random.sample({y for y in range(len(chars))}, 1)[0]
    print(chars[i], sep='', end='')