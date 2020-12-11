# Standard library imports
import re
import sys
import csv

import matrix_inv

USAGE = "Usage: {} [-i] 'infile.csv' ['outfile.csv']".format(sys.argv[0])

args_pattern = re.compile(
    r"""
    ^
    (
    (?P<HELP>-h|--help)|
    (?P<INP>-i|--input)|
    ((?P<ARG1>\w+\.csv))
    (\s(?P<ARG2>\w+\.csv$))?
    )
    $
""",
    re.VERBOSE,
)


def parse(arg_line):
    args = {}
    match_object = args_pattern.match(arg_line)
    if match_object:
        args = {k: v for k, v in match_object.groupdict().items() if v is not None}
    return args


def process_stdin():
    matrix = []
    for line in sys.stdin:
        string_list = (line.rstrip()).split(",")
        num_list = [float(string) for string in string_list]
        matrix.append(num_list)
    return matrix


def read_infile(infile):
    matrix = []
    with open(infile) as csvfile:
        for row in csv.reader(csvfile, delimiter=","):
            row = [float(val) for val in row]
            matrix.append(row)
    if len(matrix) == 0:
        raise SystemExit("Empty matrix. Please supply a valid matrix.")
    return matrix


def save_inverse(outfile, inverse):
    with open(outfile, "w", newline="") as myfile:
        wr = csv.writer(myfile, quoting=csv.QUOTE_NONE)
        for row in inverse:
            wr.writerow(row)


def main():
    args = parse(" ".join(sys.argv[1:]))
    if not args:
        raise SystemExit(USAGE)
    elif args.get("HELP"):
        print(USAGE)
        return
    elif args.get("INP"):
        matrix = process_stdin()
    else:
        matrix = read_infile(args["ARG1"])

    inverse = matrix_inv.inv(matrix)
    if args.get("ARG2"):
        save_inverse(args["ARG2"], inverse)
    else:
        input_string = """Input matrix: {}""".format(matrix)
        print(input_string)
        output_string = """Inverse matrix: {}""".format(inverse)
        print(output_string)


if __name__ == "__main__":
    main()
