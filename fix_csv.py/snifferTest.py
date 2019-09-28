import argparse
import csv

parser = argparse.ArgumentParser()

parser.add_argument("infile", help="Input file", type=str)

args = parser.parse_args()

with open(args.infile, 'r', newline='') as infile:
    dialect = csv.Sniffer().sniff(infile.read(1024))
    print("Delimiter Character: " + str(dialect.delimiter))
    print("Quote Character: " + str(dialect.quotechar))