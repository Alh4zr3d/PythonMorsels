import csv
import argparse

parser = argparse.ArgumentParser()

parser.add_argument("infile", help="Input file", type=str)
parser.add_argument("outfile", help="Output file name", type=str)
parser.add_argument("--in-delimiter", help="Specify delimiter character", type=str)
parser.add_argument("--in-quote", help="Specify quote character", type=str)

args = parser.parse_args()

with open(args.infile, 'r', newline='') as csvfile:
    dialect = csv.Sniffer().sniff(csvfile.read(1024))

if args.in_delimiter:
    delim = args.in_delimiter
else:
    delim = dialect.delimiter

if args.in_quote:
    quo = args.in_quote
else:
    quo = dialect.quotechar

with open(args.infile, "r", newline='') as infile:
    reader = csv.reader(infile, delimiter=delim, quotechar=quo)
    with open(args.outfile, "wt", newline='') as outfile:
        writer = csv.writer(outfile, delimiter=",")
        writer.writerows(reader)
